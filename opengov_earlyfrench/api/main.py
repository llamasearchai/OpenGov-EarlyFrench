"""FastAPI application for OpenGov-EarlyFrench."""

from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from opengov_earlyfrench import __version__
from opengov_earlyfrench.ai.conversation import AIConversationPartner
from opengov_earlyfrench.config import settings
from opengov_earlyfrench.core.gender_teacher import GenderTeacher
from opengov_earlyfrench.core.models import ConversationResponse, PronunciationFeedback
from opengov_earlyfrench.core.pronunciation_coach import PronunciationCoach
from opengov_earlyfrench.core.verb_conjugator import VerbConjugator
from opengov_earlyfrench.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description="AI-powered comprehensive French language learning platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    """Chat request model."""

    message: str
    level: str = "A1"


class ConjugationRequest(BaseModel):
    """Verb conjugation request."""

    verb: str
    tense: str = "présent"
    subject: Optional[str] = None


class PronunciationRequest(BaseModel):
    """Pronunciation analysis request."""

    text: str


class GenderRequest(BaseModel):
    """Gender identification request."""

    word: str


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {
        "message": "Welcome to OpenGov-EarlyFrench API",
        "version": __version__,
        "docs": "/docs",
    }


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "version": __version__}


@app.post("/api/v1/pronunciation/analyze", response_model=PronunciationFeedback)
async def analyze_pronunciation(request: PronunciationRequest) -> PronunciationFeedback:
    """Analyze pronunciation challenges in French text."""
    try:
        coach = PronunciationCoach()
        result = coach.analyze_pronunciation(request.text)
        return result
    except Exception as e:  # pragma: no cover
        logger.error(f"Pronunciation analysis error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/pronunciation/nasal-vowels")
async def teach_nasal_vowels() -> dict[str, Any]:
    """Get nasal vowel teaching content."""
    try:
        coach = PronunciationCoach()
        return coach.teach_nasal_vowels()
    except Exception as e:  # pragma: no cover
        logger.error(f"Nasal vowels error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/pronunciation/liaison/{phrase}")
async def practice_liaison(phrase: str) -> dict[str, Any]:
    """Practice liaison with a French phrase."""
    try:
        coach = PronunciationCoach()
        return coach.practice_liaison(phrase)
    except Exception as e:  # pragma: no cover
        logger.error(f"Liaison practice error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/pronunciation/minimal-pairs")
async def get_minimal_pairs() -> dict[str, Any]:
    """Get minimal pairs for pronunciation practice."""
    try:
        coach = PronunciationCoach()
        return coach.get_minimal_pairs()
    except Exception as e:  # pragma: no cover
        logger.error(f"Minimal pairs error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.post("/api/v1/verbs/conjugate")
async def conjugate_verb(request: ConjugationRequest) -> dict[str, Any]:
    """Conjugate a French verb."""
    try:
        conjugator = VerbConjugator()
        from opengov_earlyfrench.core.models import Tense

        tense_map = {
            "présent": Tense.PRESENT,
            "imparfait": Tense.IMPARFAIT,
            "futur_simple": Tense.FUTUR_SIMPLE,
            "passé_composé": Tense.PASSE_COMPOSE,
            "subjonctif_présent": Tense.SUBJUNCTIVE_PRESENT,
        }

        tense = tense_map.get(request.tense, Tense.PRESENT)
        result = conjugator.conjugate(request.verb, tense, request.subject)
        return result
    except Exception as e:  # pragma: no cover
        logger.error(f"Conjugation error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/verbs/{verb}/passe-compose/{subject}")
async def get_passe_compose(verb: str, subject: str) -> dict[str, str]:
    """Get passé composé form of a verb."""
    try:
        conjugator = VerbConjugator()
        return conjugator.form_passe_compose(verb, subject)
    except Exception as e:  # pragma: no cover
        logger.error(f"Passé composé error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/verbs/{verb}/reflexive")
async def get_reflexive_conjugation(verb: str) -> dict[str, Any]:
    """Get reflexive verb conjugation."""
    try:
        conjugator = VerbConjugator()
        return conjugator.reflexive_verb(verb)
    except Exception as e:  # pragma: no cover
        logger.error(f"Reflexive verb error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/verbs/{verb}/subjunctive")
async def practice_subjunctive(verb: str) -> dict[str, Any]:
    """Practice subjunctive mood with a verb."""
    try:
        conjugator = VerbConjugator()
        return conjugator.subjunctive_practice(verb)
    except Exception as e:  # pragma: no cover
        logger.error(f"Subjunctive practice error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.post("/api/v1/gender/identify")
async def identify_gender(request: GenderRequest) -> dict[str, Any]:
    """Identify gender pattern for a word."""
    try:
        teacher = GenderTeacher()
        return teacher.identify_pattern(request.word)
    except Exception as e:  # pragma: no cover
        logger.error(f"Gender identification error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/gender/partitive")
async def get_partitive_practice() -> dict[str, Any]:
    """Get partitive article practice."""
    try:
        teacher = GenderTeacher()
        return teacher.partitive_practice()
    except Exception as e:  # pragma: no cover
        logger.error(f"Partitive practice error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/gender/contractions")
async def get_contractions() -> dict[str, Any]:
    """Get article contraction rules."""
    try:
        teacher = GenderTeacher()
        return teacher.get_contractions()
    except Exception as e:  # pragma: no cover
        logger.error(f"Contractions error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/gender/agreement")
async def get_agreement_practice() -> dict[str, Any]:
    """Get adjective agreement practice."""
    try:
        teacher = GenderTeacher()
        return teacher.practice_agreement()
    except Exception as e:  # pragma: no cover
        logger.error(f"Agreement practice error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.post("/api/v1/conversation/chat", response_model=ConversationResponse)
async def chat_with_ai(request: ChatRequest) -> ConversationResponse:
    """Chat with AI conversation partner."""
    try:
        partner = AIConversationPartner(level=request.level)
        response = partner.chat(request.message)
        return response
    except Exception as e:  # pragma: no cover
        logger.error(f"Conversation error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


@app.get("/api/v1/conversation/scenario/{scenario_type}")
async def get_scenario(scenario_type: str) -> dict[str, Any]:
    """Get a conversation scenario."""
    try:
        partner = AIConversationPartner()
        return partner.scenario(scenario_type)
    except Exception as e:  # pragma: no cover
        logger.error(f"Scenario error: {e}")  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(e)) from e  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    import uvicorn  # pragma: no cover

    uvicorn.run(app, host=settings.api_host, port=settings.api_port)  # pragma: no cover
