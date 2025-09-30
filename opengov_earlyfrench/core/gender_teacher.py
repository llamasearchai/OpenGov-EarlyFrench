"""French gender teaching module."""

from typing import Any, Union

from opengov_earlyfrench.utils.logger import get_logger

logger = get_logger(__name__)


class GenderTeacher:
    """Teaches French noun gender patterns and rules."""

    def __init__(self) -> None:
        """Initialize gender teacher."""
        self.masculine_patterns = self._initialize_masculine_patterns()
        self.feminine_patterns = self._initialize_feminine_patterns()
        self.exceptions = self._initialize_exceptions()
        self.articles = self._initialize_articles()

    def _initialize_masculine_patterns(self) -> dict[str, dict[str, Any]]:
        """Initialize masculine gender patterns."""
        return {
            "endings": {
                "-age": {
                    "examples": ["le voyage", "le fromage", "le garage"],
                    "exceptions": ["la page", "la plage", "la cage", "l'image"],
                    "reliability": "85%",
                },
                "-ment": {
                    "examples": ["le gouvernement", "le monument", "le document"],
                    "exceptions": [],
                    "reliability": "95%",
                },
                "-isme": {
                    "examples": ["le tourisme", "le capitalisme", "le réalisme"],
                    "exceptions": [],
                    "reliability": "100%",
                },
                "-eau": {
                    "examples": ["le bureau", "le château", "le tableau"],
                    "exceptions": ["l'eau (f)", "la peau"],
                    "reliability": "90%",
                },
            },
            "categories": {
                "days": ["le lundi", "le mardi", "le mercredi"],
                "months": ["le janvier", "le février", "le mars"],
                "seasons": ["le printemps", "l'été", "l'automne", "l'hiver"],
                "languages": ["le français", "l'anglais", "l'espagnol"],
                "trees": ["le chêne", "le sapin", "le pommier"],
                "metals": ["le fer", "l'or", "l'argent"],
            },
        }

    def _initialize_feminine_patterns(self) -> dict[str, dict[str, Any]]:
        """Initialize feminine gender patterns."""
        return {
            "endings": {
                "-tion": {
                    "examples": ["la nation", "la situation", "la solution"],
                    "exceptions": [],
                    "reliability": "100%",
                },
                "-té": {
                    "examples": ["la liberté", "la société", "la qualité"],
                    "exceptions": [],
                    "reliability": "100%",
                },
                "-ité": {
                    "examples": ["la liberté", "la société", "la qualité"],
                    "exceptions": [],
                    "reliability": "100%",
                },
                "-ance/-ence": {
                    "examples": ["la chance", "la distance", "la science"],
                    "exceptions": [],
                    "reliability": "98%",
                },
                "-ure": {
                    "examples": ["la nature", "la culture", "la voiture"],
                    "exceptions": [],
                    "reliability": "95%",
                },
                "-ie": {
                    "examples": ["la vie", "la philosophie", "la boulangerie"],
                    "exceptions": ["le génie", "le parapluie"],
                    "reliability": "90%",
                },
            },
            "categories": {
                "sciences": ["la physique", "la chimie", "la biologie"],
                "continents": ["l'Europe", "l'Asie", "l'Afrique"],
                "most_countries": ["la France", "l'Allemagne", "l'Espagne"],
                "exceptions_countries": ["le Mexique", "le Canada", "le Japon"],
            },
        }

    def _initialize_exceptions(self) -> list[dict[str, str]]:
        """Initialize common exceptions to gender rules."""
        return [
            {
                "word": "le problème",
                "expected": "feminine",
                "actual": "masculine",
                "note": "Greek origin",
            },
            {
                "word": "le système",
                "expected": "feminine",
                "actual": "masculine",
                "note": "Greek origin",
            },
            {
                "word": "la victime",
                "expected": "masculine",
                "actual": "feminine",
                "note": "Always feminine even for males",
            },
            {
                "word": "la personne",
                "expected": "varies",
                "actual": "feminine",
                "note": "Always feminine",
            },
            {
                "word": "le mannequin",
                "expected": "feminine",
                "actual": "masculine",
                "note": "Always masculine",
            },
        ]

    def _initialize_articles(self) -> dict[str, Any]:
        """Initialize article forms and contractions."""
        return {
            "definite": {
                "masculine": {
                    "singular": "le",
                    "plural": "les",
                    "before_vowel": "l'",
                },
                "feminine": {
                    "singular": "la",
                    "plural": "les",
                    "before_vowel": "l'",
                },
            },
            "indefinite": {
                "masculine": {
                    "singular": "un",
                    "plural": "des",
                },
                "feminine": {
                    "singular": "une",
                    "plural": "des",
                },
            },
            "partitive": {
                "masculine": "du",
                "feminine": "de la",
                "before_vowel": "de l'",
                "plural": "des",
                "negative": "de/d'",
            },
            "contractions": {
                "à + le": "au",
                "à + les": "aux",
                "de + le": "du",
                "de + les": "des",
            },
        }

    def identify_pattern(self, word: str) -> dict[str, Union[str, bool]]:
        """Identify gender pattern for a word."""
        word_lower = word.lower().strip()

        # Check feminine patterns first (more reliable)
        for ending, data in self.feminine_patterns["endings"].items():
            endings_to_check = ending.split("/")
            for end in endings_to_check:
                end_clean = end.strip("-")
                if word_lower.endswith(end_clean):
                    exceptions = data.get("exceptions", [])
                    is_exception = any(ex.replace("l'", "").replace("la ", "").replace("le ", "") in word_lower for ex in exceptions)
                    return {
                        "word": word,
                        "likely_gender": "masculine" if is_exception else "feminine",
                        "rule": f"Words ending in {ending} are usually feminine",
                        "reliability": data["reliability"],
                        "is_exception": is_exception,
                    }

        # Check masculine patterns
        for ending, data in self.masculine_patterns["endings"].items():
            end_clean = ending.strip("-")
            if word_lower.endswith(end_clean):
                exceptions = data.get("exceptions", [])
                is_exception = any(ex.replace("l'", "").replace("la ", "").replace("le ", "") in word_lower for ex in exceptions)
                return {
                    "word": word,
                    "likely_gender": "feminine" if is_exception else "masculine",
                    "rule": f"Words ending in {ending} are usually masculine",
                    "reliability": data["reliability"],
                    "is_exception": is_exception,
                }

        return {
            "word": word,
            "likely_gender": "unknown",
            "rule": "No clear pattern detected - memorization needed",
            "tip": "Use context and practice to remember",
        }

    def partitive_practice(self) -> dict[str, Union[str, dict[str, str], list[str]]]:
        """Practice partitive articles."""
        return {
            "explanation": "Partitive articles express 'some' or 'any' in French",
            "forms": self.articles["partitive"],
            "examples": {
                "du pain": "some bread (masculine)",
                "de la viande": "some meat (feminine)",
                "de l'eau": "some water (before vowel)",
                "des fruits": "some fruits (plural)",
                "pas de sucre": "no sugar (negative)",
            },
            "rules": [
                "Use du with masculine singular",
                "Use de la with feminine singular",
                "Use de l' before vowels",
                "Use des for plural",
                "After negative, use de/d' only",
            ],
            "practice_sentences": [
                "Je voudrais du café - I would like some coffee",
                "Il n'y a pas de lait - There is no milk",
                "Elle mange des légumes - She eats vegetables",
            ],
        }

    def get_contractions(self) -> dict[str, Union[dict[str, str], list[str], str]]:
        """Get article contraction rules."""
        return {
            "rules": self.articles["contractions"],
            "examples": {
                "au": {
                    "formation": "à + le → au",
                    "example": "Je vais au cinéma (à + le cinéma)",
                },
                "aux": {
                    "formation": "à + les → aux",
                    "example": "Je parle aux enfants (à + les enfants)",
                },
                "du": {
                    "formation": "de + le → du",
                    "example": "Le livre du professeur (de + le professeur)",
                },
                "des": {
                    "formation": "de + les → des",
                    "example": "La voiture des voisins (de + les voisins)",
                },
            },
            "no_contraction": [
                "à la → à la (no change)",
                "de la → de la (no change)",
                "à l' → à l' (before vowel)",
                "de l' → de l' (before vowel)",
            ],
            "tip": "Contractions only happen with le and les, not with la or l'",
        }

    def practice_agreement(self) -> dict[str, dict[str, Any]]:
        """Practice adjective agreement with gender."""
        return {
            "rules": {
                "basic": "Adjectives must agree in gender and number with the noun",
                "feminine": "Usually add -e to masculine form",
                "plural": "Usually add -s to singular form",
                "feminine_plural": "Add -es to masculine singular",
            },
            "examples": {
                "petit": {
                    "masculine_singular": "un petit garçon",
                    "feminine_singular": "une petite fille",
                    "masculine_plural": "des petits garçons",
                    "feminine_plural": "des petites filles",
                },
                "intelligent": {
                    "masculine_singular": "un homme intelligent",
                    "feminine_singular": "une femme intelligente",
                    "masculine_plural": "des hommes intelligents",
                    "feminine_plural": "des femmes intelligentes",
                },
            },
            "special_cases": {
                "beau": "beau → belle (irregular)",
                "nouveau": "nouveau → nouvelle (irregular)",
                "vieux": "vieux → vieille (irregular)",
                "endings_in_eux": "-eux → -euse (heureux → heureuse)",
                "endings_in_er": "-er → -ère (premier → première)",
            },
        }
