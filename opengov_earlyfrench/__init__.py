"""OpenGov-EarlyFrench - Comprehensive AI-powered French language learning platform."""

__version__ = "0.1.0"
__author__ = "Nik Jois"
__email__ = "nikjois@llamasearch.ai"

from opengov_earlyfrench.ai.conversation import AIConversationPartner
from opengov_earlyfrench.config import settings
from opengov_earlyfrench.core.gender_teacher import GenderTeacher
from opengov_earlyfrench.core.pronunciation_coach import PronunciationCoach
from opengov_earlyfrench.core.verb_conjugator import VerbConjugator

__all__ = [
    "AIConversationPartner",
    "GenderTeacher",
    "PronunciationCoach",
    "VerbConjugator",
    "__version__",
    "settings",
]

