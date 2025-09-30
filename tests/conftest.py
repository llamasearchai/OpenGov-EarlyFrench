"""Pytest configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient

from opengov_earlyfrench.ai.conversation import AIConversationPartner
from opengov_earlyfrench.api.main import app
from opengov_earlyfrench.core.gender_teacher import GenderTeacher
from opengov_earlyfrench.core.pronunciation_coach import PronunciationCoach
from opengov_earlyfrench.core.verb_conjugator import VerbConjugator


@pytest.fixture
def api_client() -> TestClient:
    """Create FastAPI test client."""
    return TestClient(app)


@pytest.fixture
def pronunciation_coach() -> PronunciationCoach:
    """Create pronunciation coach instance."""
    return PronunciationCoach()


@pytest.fixture
def verb_conjugator() -> VerbConjugator:
    """Create verb conjugator instance."""
    return VerbConjugator()


@pytest.fixture
def gender_teacher() -> GenderTeacher:
    """Create gender teacher instance."""
    return GenderTeacher()


@pytest.fixture
def conversation_partner() -> AIConversationPartner:
    """Create AI conversation partner instance."""
    return AIConversationPartner(level="A1")
