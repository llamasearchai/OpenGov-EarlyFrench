"""Core data models for French language learning."""
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class CEFRLevel(str, Enum):
    """CEFR proficiency levels."""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"


class Gender(str, Enum):
    """French grammatical genders."""

    MASCULINE = "masculine"
    FEMININE = "feminine"


class Formality(str, Enum):
    """Formality levels."""

    INFORMAL = "informal"
    FORMAL = "formal"


class VerbGroup(str, Enum):
    """French verb groups."""

    FIRST = "first"
    SECOND = "second"
    THIRD = "third"


class Tense(str, Enum):
    """French tenses."""

    PRESENT = "présent"
    PASSE_COMPOSE = "passé_composé"
    IMPARFAIT = "imparfait"
    PLUS_QUE_PARFAIT = "plus_que_parfait"
    FUTUR_SIMPLE = "futur_simple"
    FUTUR_ANTERIEUR = "futur_antérieur"
    PASSE_SIMPLE = "passé_simple"
    PASSE_ANTERIEUR = "passé_antérieur"
    CONDITIONAL_PRESENT = "conditionnel_présent"
    CONDITIONAL_PAST = "conditionnel_passé"
    SUBJUNCTIVE_PRESENT = "subjonctif_présent"
    SUBJUNCTIVE_PAST = "subjonctif_passé"
    SUBJUNCTIVE_IMPERFECT = "subjonctif_imparfait"
    SUBJUNCTIVE_PLUPERFECT = "subjonctif_plus_que_parfait"


class Verb(BaseModel):
    """French verb model."""

    id: str = Field(description="Verb ID")
    infinitive: str = Field(description="Infinitive form")
    english: str = Field(description="English translation")
    verb_group: VerbGroup = Field(description="Verb group")

    is_reflexive: bool = Field(default=False)
    auxiliary_verb: str = Field(default="avoir", description="avoir or être")

    conjugations: dict[str, dict[str, str]] = Field(
        default_factory=dict, description="Conjugations by tense and person"
    )

    past_participle: str = Field(description="Past participle")
    present_participle: str = Field(description="Present participle")

    imperative: dict[str, str] = Field(default_factory=dict)

    example_sentences: list[dict[str, str]] = Field(default_factory=list)

    level: CEFRLevel = Field(description="CEFR level")
    frequency_rank: Optional[int] = None


class PronunciationFeedback(BaseModel):
    """Pronunciation analysis feedback."""

    text: str = Field(description="Analyzed text")
    challenges: list[str] = Field(description="Identified challenges")
    score: float = Field(description="Pronunciation score 0-100")
    improvements: list[str] = Field(description="Suggested improvements")


class LessonResponse(BaseModel):
    """Generic lesson response."""

    title: str = Field(description="Lesson title")
    content: dict[str, Any] = Field(description="Lesson content")
    exercises: list[dict[str, Any]] = Field(default_factory=list)
    tips: list[str] = Field(default_factory=list)


class ConversationResponse(BaseModel):
    """AI conversation response."""

    french: str = Field(description="Response in French")
    english: str = Field(description="English translation")
    grammar_notes: list[str] = Field(default_factory=list)
    vocabulary: list[str] = Field(default_factory=list)
    cultural_tips: list[str] = Field(default_factory=list)
    corrections: list[str] = Field(default_factory=list)
    pronunciation_tips: list[str] = Field(default_factory=list)
    follow_up: str = Field(default="", description="Follow-up question")
