"""French pronunciation coaching module."""

from typing import Union

from opengov_earlyfrench.core.models import PronunciationFeedback
from opengov_earlyfrench.utils.logger import get_logger

logger = get_logger(__name__)


class PronunciationCoach:
    """French pronunciation teaching and coaching."""

    def __init__(self) -> None:
        """Initialize pronunciation coach."""
        self.nasal_vowels = self._initialize_nasal_vowels()
        self.silent_letters = self._initialize_silent_letters()
        self.special_sounds = self._initialize_special_sounds()
        self.accent_marks = self._initialize_accent_marks()

    def _initialize_nasal_vowels(self) -> dict[str, dict[str, Union[str, list[str], dict[str, str]]]]:
        """Initialize nasal vowel patterns and examples."""
        return {
            "an": {
                "ipa": "/ɑ̃/",
                "spellings": ["an", "am", "en", "em"],
                "examples": {
                    "dans": "in",
                    "chambre": "room",
                    "enfant": "child",
                    "temps": "time",
                },
                "tips": "Round your lips and let air flow through nose",
                "common_mistakes": "Don't pronounce the 'n' separately",
            },
            "in": {
                "ipa": "/ɛ̃/",
                "spellings": ["in", "im", "ein", "ain", "aim", "yn", "ym"],
                "examples": {
                    "vin": "wine",
                    "impossible": "impossible",
                    "plein": "full",
                    "pain": "bread",
                    "faim": "hunger",
                },
                "tips": "Smile slightly while nasalizing",
            },
            "on": {
                "ipa": "/ɔ̃/",
                "spellings": ["on", "om"],
                "examples": {
                    "bon": "good",
                    "nom": "name",
                    "maison": "house",
                    "comprendre": "understand",
                },
                "tips": "Round lips as for 'o' but nasalize",
            },
            "un": {
                "ipa": "/œ̃/ or /ɛ̃/",
                "spellings": ["un", "um"],
                "examples": {
                    "un": "one/a",
                    "brun": "brown",
                    "parfum": "perfume",
                    "lundi": "Monday",
                },
                "tips": "In many regions, now pronounced like 'in'",
                "note": "Distinction disappearing in modern French",
            },
        }

    def _initialize_silent_letters(self) -> dict[str, dict[str, Union[str, list[str], dict[str, str]]]]:
        """Initialize silent letter rules."""
        return {
            "final_consonants": {
                "rule": "Most final consonants are silent",
                "exceptions": ["c", "r", "f", "l"],
                "examples": {
                    "petit": "peh-TEE (t is silent)",
                    "beaucoup": "boh-KOO (p is silent)",
                    "avec": "ah-VEK (c is pronounced)",
                    "amour": "ah-MOOR (r is pronounced)",
                },
            },
            "h": {
                "rule": "H is always silent in French",
                "types": {
                    "h_muet": {
                        "description": "Silent h, allows liaison",
                        "examples": ["l'homme", "l'histoire"],
                    },
                    "h_aspiré": {
                        "description": "Aspirated h, prevents liaison",
                        "examples": ["le haricot", "la honte"],
                        "marked_in_dictionary": "Usually marked with *",
                    },
                },
            },
            "e_muet": {
                "rule": "Final 'e' often silent or very light",
                "examples": {
                    "table": "TAHBL",
                    "libre": "LEEBR",
                    "je mange": "zhuh MAHNZH",
                },
                "exception": "Pronounced in songs and poetry",
            },
        }

    def _initialize_special_sounds(self) -> dict[str, dict[str, Union[str, list[str], dict[str, str]]]]:
        """Initialize special French sounds."""
        return {
            "r": {
                "ipa": "/ʁ/",
                "description": "Uvular fricative (back of throat)",
                "tips": [
                    "Gargle lightly without water",
                    "Air vibrates at back of throat",
                    "Not rolled like Spanish R",
                ],
                "practice_words": ["rouge", "rue", "trois", "français"],
            },
            "u": {
                "ipa": "/y/",
                "description": "Rounded front vowel",
                "tips": [
                    "Say 'ee' then round your lips",
                    "Keep tongue forward",
                    "Not like English 'oo'",
                ],
                "practice_words": ["tu", "rue", "sûr", "mur"],
            },
            "eu": {
                "ipa": "/ø/ or /œ/",
                "closed": {
                    "sound": "/ø/",
                    "examples": ["peu", "deux", "feu"],
                    "tip": "Lips rounded, tongue mid-position",
                },
                "open": {
                    "sound": "/œ/",
                    "examples": ["peur", "seul", "fleur"],
                    "tip": "More open than closed 'eu'",
                },
            },
            "oi": {
                "ipa": "/wa/",
                "examples": ["moi", "toi", "boire", "voir"],
                "tip": "Pronounced like 'wah'",
            },
        }

    def _initialize_accent_marks(self) -> dict[str, dict[str, Union[str, list[str]]]]:
        """Initialize accent mark effects on pronunciation."""
        return {
            "é": {
                "name": "accent aigu",
                "sound": "/e/",
                "examples": ["été", "café", "télé"],
                "tip": "Closed 'e' sound like 'ay'",
            },
            "è": {
                "name": "accent grave",
                "sound": "/ɛ/",
                "examples": ["père", "mère", "très"],
                "tip": "Open 'e' sound like 'eh'",
            },
            "ê": {
                "name": "accent circonflexe",
                "sound": "/ɛ/",
                "examples": ["être", "fenêtre", "forêt"],
                "tip": "Open 'e', often marks lost 's'",
                "history": "feste → fête, hospital → hôpital",
            },
            "ç": {
                "name": "cédille",
                "sound": "/s/",
                "examples": ["français", "ça", "leçon"],
                "tip": "Makes 'c' soft before a, o, u",
            },
        }

    def teach_nasal_vowels(self) -> dict[str, Union[str, dict[str, dict[str, Union[str, list[str], dict[str, str]]]], list[str]]]:
        """Teach nasal vowel pronunciation."""
        return {
            "explanation": "Nasal vowels are unique to French - air flows through nose",
            "vowels": self.nasal_vowels,
            "practice_phrases": [
                "Un bon vin blanc - A good white wine",
                "Mon oncle et ma tante - My uncle and aunt",
                "Il prend son temps - He takes his time",
            ],
            "tips": [
                "Don't pronounce the 'n' or 'm' - they just nasalize the vowel",
                "Practice with a mirror to see air fog",
                "Hold your nose - you shouldn't be able to say them properly",
            ],
        }

    def practice_liaison(self, phrase: str) -> dict[str, str]:
        """Practice liaison in French phrases."""
        liaison_examples = {
            "les amis": {
                "pronunciation": "lay-zah-MEE",
                "rule": "s → /z/ before vowel",
                "type": "obligatory",
            },
            "petit ami": {
                "pronunciation": "puh-tee-tah-MEE",
                "rule": "t → /t/ before vowel",
                "type": "obligatory",
            },
            "vous avez": {
                "pronunciation": "voo-zah-VEH",
                "rule": "s → /z/ between pronoun and verb",
                "type": "obligatory",
            },
            "deux heures": {
                "pronunciation": "deu-ZEUR",
                "rule": "x → /z/ before vowel",
                "type": "obligatory",
            },
            "grand homme": {
                "pronunciation": "grahn-TOM",
                "rule": "d → /t/ before vowel",
                "type": "obligatory",
            },
        }

        if phrase.lower() in liaison_examples:
            example = liaison_examples[phrase.lower()]
            return {
                "phrase": phrase,
                "pronunciation": example["pronunciation"],
                "rule": example["rule"],
                "type": example["type"],
                "explanation": "The final consonant links to the next word starting with a vowel",
            }

        return {
            "phrase": phrase,
            "tip": "Check if there's a consonant before a vowel sound",
            "common_liaisons": ", ".join(list(liaison_examples.keys())),
        }

    def analyze_pronunciation(self, text: str) -> PronunciationFeedback:
        """Analyze pronunciation challenges in text."""
        challenges = []

        for _nasal, data in self.nasal_vowels.items():
            spellings = data.get("spellings", [])
            if isinstance(spellings, list):
                for spelling in spellings:
                    if spelling in text.lower():
                        ipa = data.get("ipa", "")
                        challenges.append(f"Nasal vowel '{spelling}' → {ipa}")

        if any(text.lower().endswith(c) for c in ["t", "d", "s", "x", "z", "p"]):
            challenges.append("Final consonant likely silent")

        if "r" in text.lower():
            challenges.append("French 'r' sound /ʁ/")

        if "u" in text.lower():
            challenges.append("French 'u' sound /y/")

        return PronunciationFeedback(
            text=text,
            challenges=challenges,
            score=max(0.0, 100.0 - len(challenges) * 10.0),
            improvements=[
                "Practice nasal vowels separately",
                "Focus on French 'r' production",
                "Remember silent final consonants",
            ],
        )

    def get_minimal_pairs(self) -> dict[str, dict[str, Union[str, list[dict[str, str]]]]]:
        """Get minimal pairs for pronunciation practice."""
        return {
            "u_vs_ou": {
                "pairs": [
                    {"u": "tu", "ou": "tout"},
                    {"u": "rue", "ou": "roue"},
                    {"u": "su", "ou": "sous"},
                ],
                "tip": "U is front rounded, OU is back rounded",
            },
            "é_vs_è": {
                "pairs": [
                    {"é": "été", "è": "être"},
                    {"é": "fée", "è": "fait"},
                    {"é": "pré", "è": "près"},
                ],
                "tip": "É is closed, È is open",
            },
            "an_vs_on": {
                "pairs": [
                    {"an": "sans", "on": "son"},
                    {"an": "banc", "on": "bon"},
                    {"an": "vent", "on": "vont"},
                ],
                "tip": "Different nasal vowels - practice separately",
            },
        }
