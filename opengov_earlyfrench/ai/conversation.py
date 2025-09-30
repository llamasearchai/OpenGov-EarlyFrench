"""AI-powered French conversation partner."""

import json
from typing import Any

from openai import OpenAI

from opengov_earlyfrench.config import settings
from opengov_earlyfrench.core.models import CEFRLevel, ConversationResponse, Formality
from opengov_earlyfrench.utils.logger import get_logger

logger = get_logger(__name__)


class AIConversationPartner:
    """AI conversation partner for French practice."""

    def __init__(self, level: str = "A1") -> None:
        """Initialize AI conversation partner."""
        self.level = CEFRLevel(level)
        try:
            self.client = OpenAI(api_key=settings.openai_api_key.get_secret_value())
        except Exception as e:  # pragma: no cover - environment dependent
            logger.warning(f"OpenAI client initialization failed: {e}")  # pragma: no cover
            self.client = None
        self.conversation_history: list[dict[str, str]] = []
        self.formality = Formality.FORMAL

    def chat(self, user_input: str) -> ConversationResponse:
        """Chat with the AI partner."""
        self.conversation_history.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = self._generate_response(user_input)

        self.conversation_history.append(
            {
                "role": "assistant",
                "content": response.french,
            }
        )

        return response

    def _generate_response(self, user_input: str) -> ConversationResponse:
        """Generate AI response."""
        if not self.client:
            return ConversationResponse(
                french="Désolé, le service n'est pas disponible.",
                english="Sorry, the service is not available.",
                grammar_notes=[],
                vocabulary=[],
                cultural_tips=[],
                corrections=[],
                pronunciation_tips=[],
                follow_up="",
            )

        try:  # pragma: no cover - uses external API
            system_prompt = self._build_system_prompt()

            messages = [
                {"role": "system", "content": system_prompt},
            ]

            for msg in self.conversation_history[-5:]:
                messages.append(msg)

            response = self.client.chat.completions.create(  # pragma: no cover - external API
                model=settings.openai_model,
                messages=messages,
                temperature=settings.openai_temperature,
                max_tokens=settings.openai_max_tokens,
            )

            content = response.choices[0].message.content or ""

            try:  # pragma: no cover - parsing external model output
                data = json.loads(content)
                return ConversationResponse(
                    french=data.get("french", ""),
                    english=data.get("english", ""),
                    grammar_notes=data.get("grammar_notes", []),
                    vocabulary=data.get("vocabulary", []),
                    cultural_tips=data.get("cultural_tips", []),
                    corrections=data.get("corrections", []),
                    pronunciation_tips=data.get("pronunciation_tips", []),
                    follow_up=data.get("follow_up", ""),
                )
            except json.JSONDecodeError:  # pragma: no cover - pass-through path
                return ConversationResponse(
                    french=content,
                    english="",
                    grammar_notes=[],
                    vocabulary=[],
                    cultural_tips=[],
                    corrections=[],
                    pronunciation_tips=[],
                    follow_up="",
                )

        except Exception as e:  # pragma: no cover - external API failure
            logger.error(f"Error generating response: {e}")  # pragma: no cover
            return ConversationResponse(  # pragma: no cover
                french="Pardon, je n'ai pas compris. Pouvez-vous répéter ?",
                english="Sorry, I didn't understand. Can you repeat?",
                grammar_notes=[],
                vocabulary=[],
                cultural_tips=[],
                corrections=[],
                pronunciation_tips=[],
                follow_up="",
            )

    def _build_system_prompt(self) -> str:
        """Build system prompt for AI."""
        level_descriptions = {
            CEFRLevel.A1: "absolute beginner - use very simple vocabulary, present tense, basic phrases",
            CEFRLevel.A2: "elementary - use basic vocabulary, present/passé composé, simple sentences",
            CEFRLevel.B1: "intermediate - use everyday vocabulary, various tenses, longer sentences",
            CEFRLevel.B2: "upper intermediate - use complex sentences, subjunctive, idiomatic expressions",
            CEFRLevel.C1: "advanced - use sophisticated vocabulary, all tenses, nuanced expressions",
            CEFRLevel.C2: "proficiency - use native-like expressions, cultural references, wordplay",
        }

        formality_instruction = (
            "Use vous (formal) form"
            if self.formality == Formality.FORMAL
            else "Use tu (informal) form"
        )

        return f"""
        You are a friendly French conversation partner for a {level_descriptions[self.level]} student.

        Your responses should:
        1. Be appropriate for {self.level} level
        2. Use natural, conversational French
        3. {formality_instruction}
        4. Gradually introduce new vocabulary
        5. Correct errors gently
        6. Be encouraging and supportive
        7. Include cultural context when relevant
        8. Pay attention to gender agreement and verb conjugations

        Format your response as JSON:
        {{
            "french": "Your response in French",
            "english": "English translation",
            "grammar_notes": ["grammar points used"],
            "vocabulary": ["new words with gender if nouns"],
            "cultural_tips": ["cultural context if relevant"],
            "corrections": ["gentle corrections if needed"],
            "pronunciation_tips": ["any pronunciation advice"],
            "follow_up": "A follow-up question to continue conversation"
        }}

        Keep responses natural and conversational. Use appropriate French expressions.
        """

    def scenario(self, scenario_type: str) -> dict[str, Any]:
        """Start a specific conversation scenario."""
        scenarios: dict[str, dict[str, Any]] = {
            "café": {
                "setting": "You're at a Parisian café",
                "starter": "Bonjour ! Qu'est-ce que je vous sers ?",
                "english": "Hello! What can I serve you?",
                "vocabulary": {
                    "un café": "coffee",
                    "un expresso": "espresso",
                    "un café crème": "coffee with milk",
                    "un croissant": "croissant",
                    "l'addition (f)": "the bill",
                },
                "useful_phrases": [
                    "Je voudrais... - I would like...",
                    "Un café, s'il vous plaît - A coffee, please",
                    "Combien ça coûte ? - How much does it cost?",
                    "L'addition, s'il vous plaît - The bill, please",
                ],
                "cultural_tips": [
                    "Coffee is typically served after meals, not during",
                    "Un café means espresso, not American coffee",
                    "Tipping is appreciated but not obligatory (round up)",
                ],
            },
            "marché": {
                "setting": "You're at a French market",
                "starter": "Bonjour madame/monsieur ! Vous désirez ?",
                "english": "Hello madam/sir! What would you like?",
                "vocabulary": {
                    "les fruits (m)": "fruits",
                    "les légumes (m)": "vegetables",
                    "le kilo": "kilogram",
                    "la livre": "pound (500g)",
                    "frais/fraîche": "fresh",
                },
                "useful_phrases": [
                    "Je voudrais un kilo de... - I'd like a kilo of...",
                    "C'est combien le kilo ? - How much per kilo?",
                    "Ils sont mûrs ? - Are they ripe?",
                    "C'est tout, merci - That's all, thanks",
                ],
            },
        }

        scenario = scenarios.get(scenario_type, scenarios["café"])

        return {
            "dialogue": scenario["starter"],
            "english": scenario["english"],
            "setting": scenario["setting"],
            "vocabulary": scenario["vocabulary"],
            "useful_phrases": scenario["useful_phrases"],
            "cultural_tips": scenario.get("cultural_tips", []),
        }
