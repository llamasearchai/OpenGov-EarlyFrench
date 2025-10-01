"""French verb conjugation system."""

from typing import Optional, Union

from opengov_earlyfrench.core.models import CEFRLevel, Tense, Verb, VerbGroup
from opengov_earlyfrench.utils.logger import get_logger

logger = get_logger(__name__)


class VerbConjugator:
    """French verb conjugation engine."""

    def __init__(self) -> None:
        """Initialize verb conjugator."""
        self.regular_endings = self._load_regular_endings()
        self.irregular_verbs = self._load_irregular_verbs()
        self.auxiliary_rules = self._load_auxiliary_rules()

    def _load_regular_endings(self) -> dict[VerbGroup, dict[Tense, dict[str, str]]]:
        """Load regular verb endings by group and tense."""
        return {
            VerbGroup.FIRST: {
                Tense.PRESENT: {
                    "je": "e",
                    "tu": "es",
                    "il/elle/on": "e",
                    "nous": "ons",
                    "vous": "ez",
                    "ils/elles": "ent",
                },
                Tense.IMPARFAIT: {
                    "je": "ais",
                    "tu": "ais",
                    "il/elle/on": "ait",
                    "nous": "ions",
                    "vous": "iez",
                    "ils/elles": "aient",
                },
                Tense.FUTUR_SIMPLE: {
                    "je": "erai",
                    "tu": "eras",
                    "il/elle/on": "era",
                    "nous": "erons",
                    "vous": "erez",
                    "ils/elles": "eront",
                },
            },
            VerbGroup.SECOND: {
                Tense.PRESENT: {
                    "je": "is",
                    "tu": "is",
                    "il/elle/on": "it",
                    "nous": "issons",
                    "vous": "issez",
                    "ils/elles": "issent",
                },
            },
            VerbGroup.THIRD: {
                Tense.PRESENT: {
                    "je": "s",
                    "tu": "s",
                    "il/elle/on": "",
                    "nous": "ons",
                    "vous": "ez",
                    "ils/elles": "ent",
                },
            },
        }

    def _load_irregular_verbs(self) -> dict[str, Verb]:
        """Load irregular verb database."""
        irregulars: dict[str, Verb] = {}

        irregulars["être"] = Verb(
            id="verb_être",
            infinitive="être",
            english="to be",
            verb_group=VerbGroup.THIRD,
            auxiliary_verb="avoir",
            conjugations={
                Tense.PRESENT.value: {
                    "je": "suis",
                    "tu": "es",
                    "il/elle/on": "est",
                    "nous": "sommes",
                    "vous": "êtes",
                    "ils/elles": "sont",
                },
                Tense.IMPARFAIT.value: {
                    "je": "étais",
                    "tu": "étais",
                    "il/elle/on": "était",
                    "nous": "étions",
                    "vous": "étiez",
                    "ils/elles": "étaient",
                },
                Tense.FUTUR_SIMPLE.value: {
                    "je": "serai",
                    "tu": "seras",
                    "il/elle/on": "sera",
                    "nous": "serons",
                    "vous": "serez",
                    "ils/elles": "seront",
                },
                Tense.SUBJUNCTIVE_PRESENT.value: {
                    "que je": "sois",
                    "que tu": "sois",
                    "qu'il/elle/on": "soit",
                    "que nous": "soyons",
                    "que vous": "soyez",
                    "qu'ils/elles": "soient",
                },
            },
            past_participle="été",
            present_participle="étant",
            level=CEFRLevel.A1,
        )

        irregulars["avoir"] = Verb(
            id="verb_avoir",
            infinitive="avoir",
            english="to have",
            verb_group=VerbGroup.THIRD,
            auxiliary_verb="avoir",
            conjugations={
                Tense.PRESENT.value: {
                    "j'": "ai",
                    "tu": "as",
                    "il/elle/on": "a",
                    "nous": "avons",
                    "vous": "avez",
                    "ils/elles": "ont",
                },
                Tense.IMPARFAIT.value: {
                    "j'": "avais",
                    "tu": "avais",
                    "il/elle/on": "avait",
                    "nous": "avions",
                    "vous": "aviez",
                    "ils/elles": "avaient",
                },
                Tense.FUTUR_SIMPLE.value: {
                    "j'": "aurai",
                    "tu": "auras",
                    "il/elle/on": "aura",
                    "nous": "aurons",
                    "vous": "aurez",
                    "ils/elles": "auront",
                },
                Tense.SUBJUNCTIVE_PRESENT.value: {
                    "que j'": "aie",
                    "que tu": "aies",
                    "qu'il/elle/on": "ait",
                    "que nous": "ayons",
                    "que vous": "ayez",
                    "qu'ils/elles": "aient",
                },
            },
            past_participle="eu",
            present_participle="ayant",
            level=CEFRLevel.A1,
        )

        irregulars["aller"] = Verb(
            id="verb_aller",
            infinitive="aller",
            english="to go",
            verb_group=VerbGroup.THIRD,
            auxiliary_verb="être",
            conjugations={
                Tense.PRESENT.value: {
                    "je": "vais",
                    "tu": "vas",
                    "il/elle/on": "va",
                    "nous": "allons",
                    "vous": "allez",
                    "ils/elles": "vont",
                },
                Tense.IMPARFAIT.value: {
                    "j'": "allais",
                    "tu": "allais",
                    "il/elle/on": "allait",
                    "nous": "allions",
                    "vous": "alliez",
                    "ils/elles": "allaient",
                },
                Tense.FUTUR_SIMPLE.value: {
                    "j'": "irai",
                    "tu": "iras",
                    "il/elle/on": "ira",
                    "nous": "irons",
                    "vous": "irez",
                    "ils/elles": "iront",
                },
            },
            past_participle="allé",
            present_participle="allant",
            level=CEFRLevel.A1,
        )

        irregulars["faire"] = Verb(
            id="verb_faire",
            infinitive="faire",
            english="to do/make",
            verb_group=VerbGroup.THIRD,
            auxiliary_verb="avoir",
            conjugations={
                Tense.PRESENT.value: {
                    "je": "fais",
                    "tu": "fais",
                    "il/elle/on": "fait",
                    "nous": "faisons",
                    "vous": "faites",
                    "ils/elles": "font",
                },
            },
            past_participle="fait",
            present_participle="faisant",
            level=CEFRLevel.A1,
        )

        return irregulars

    def _load_auxiliary_rules(self) -> dict[str, dict[str, Union[str, bool, list[str]]]]:
        """Load rules for auxiliary verb selection."""
        return {
            "être_verbs": {
                "movement": ["aller", "venir", "arriver", "partir", "entrer", "sortir"],
                "state_change": ["naître", "mourir", "devenir", "rester"],
                "all_reflexive": True,
                "mnemonic": "DR & MRS VANDERTRAMP",
                "list": [
                    "devenir",
                    "revenir",
                    "monter",
                    "rentrer",
                    "sortir",
                    "venir",
                    "aller",
                    "naître",
                    "descendre",
                    "entrer",
                    "retourner",
                    "tomber",
                    "rester",
                    "arriver",
                    "mourir",
                    "partir",
                ],
            },
            "agreement_rules": {
                "with_être": "Past participle agrees with subject",
                "with_avoir": "Past participle agrees with preceding direct object",
                "examples": {
                    "être": "Elle est allée (feminine singular)",
                    "avoir": "Les fleurs que j'ai achetées (feminine plural object before)",
                },
            },
        }

    def conjugate(
        self, infinitive: str, tense: Tense = Tense.PRESENT, subject: Optional[str] = None
    ) -> dict[str, Union[str, dict[str, str]]]:
        """Conjugate a French verb."""
        if infinitive in self.irregular_verbs:
            verb = self.irregular_verbs[infinitive]
            if tense.value in verb.conjugations:
                forms = verb.conjugations[tense.value]

                if subject:
                    return {
                        "infinitive": infinitive,
                        "tense": tense.value,
                        "subject": subject,
                        "form": forms.get(subject, "Form not found"),
                    }

                return {
                    "infinitive": infinitive,
                    "tense": tense.value,
                    "forms": forms,
                    "type": "irregular",
                    "auxiliary": verb.auxiliary_verb,
                    "past_participle": verb.past_participle,
                }

        verb_group = self._determine_verb_group(infinitive)
        stem = self._get_stem(infinitive, verb_group)

        if verb_group in self.regular_endings and tense in self.regular_endings[verb_group]:
            endings = self.regular_endings[verb_group][tense]
            forms = {}

            for pronoun, ending in endings.items():
                if (
                    pronoun == "je"
                    and (stem + ending)
                    and (stem + ending)[0] in ("a", "e", "i", "o", "u", "h")
                ):
                    forms["j'"] = stem + ending
                else:
                    forms[pronoun] = stem + ending

            return {
                "infinitive": infinitive,
                "tense": tense.value,
                "forms": forms,
                "type": "regular",
                "group": verb_group.value,
            }

        return {"error": f"Cannot conjugate {infinitive} in {tense.value}"}

    def _determine_verb_group(self, infinitive: str) -> VerbGroup:
        """Determine verb group from infinitive."""
        if infinitive.endswith("er"):
            return VerbGroup.FIRST
        elif infinitive.endswith("ir"):
            return VerbGroup.SECOND
        else:
            return VerbGroup.THIRD

    def _get_stem(self, infinitive: str, group: VerbGroup) -> str:
        """Get verb stem from infinitive."""
        if group in (VerbGroup.FIRST, VerbGroup.SECOND):
            return infinitive[:-2]
        else:
            return infinitive[:-2] if infinitive.endswith("re") else infinitive[:-3]

    def form_passe_compose(self, infinitive: str, subject: str) -> dict[str, str]:
        """Form passé composé for a verb."""
        etre_list = self.auxiliary_rules["être_verbs"].get("list", [])
        auxiliary = "être" if infinitive.lower() in etre_list else "avoir"

        # Get auxiliary conjugation without specific subject first
        aux_conj = self.conjugate(auxiliary, Tense.PRESENT)

        # Get the form for the specific subject
        aux_form = ""
        if isinstance(aux_conj.get("forms"), dict):
            forms = aux_conj["forms"]
            # Try to find matching subject
            if subject in forms:
                aux_form = forms[subject]
            elif f"{subject[0]}'" in forms:  # Handle j'
                aux_form = forms[f"{subject[0]}'"]
            else:
                # Try different variations
                for key in forms:
                    if subject in key:
                        aux_form = forms[key]
                        break

        if infinitive in self.irregular_verbs:
            past_part = self.irregular_verbs[infinitive].past_participle
        else:
            group = self._determine_verb_group(infinitive)
            stem = self._get_stem(infinitive, group)

            if group == VerbGroup.FIRST:
                past_part = stem + "é"
            elif group == VerbGroup.SECOND:
                past_part = stem + "i"
            else:
                past_part = stem + "u"

        if auxiliary == "être":
            if subject in ["elle", "elles"]:
                past_part += "e"
            if subject in ["ils", "elles"]:
                past_part += "s"

        return {
            "infinitive": infinitive,
            "tense": "passé composé",
            "subject": subject,
            "auxiliary": auxiliary,
            "auxiliary_form": aux_form,
            "past_participle": past_part,
            "complete_form": f"{aux_form} {past_part}",
        }

    def reflexive_verb(self, infinitive: str) -> dict[str, Union[str, dict[str, str]]]:
        """Handle reflexive verb conjugation."""
        base_verb = (
            infinitive[3:] if infinitive.startswith("se ") else infinitive.replace("se ", "")
        )

        reflexive_pronouns = {
            "je": "me",
            "tu": "te",
            "il/elle/on": "se",
            "nous": "nous",
            "vous": "vous",
            "ils/elles": "se",
        }

        conjugation = self.conjugate(base_verb, Tense.PRESENT)

        reflexive_forms = {}
        forms_dict = conjugation.get("forms", {})
        if isinstance(forms_dict, dict):
            for subject, form in forms_dict.items():
                pronoun = reflexive_pronouns.get(subject, "se")

                if subject == "je" and form and form[0] in ("a", "e", "i", "o", "u", "h"):
                    reflexive_forms["je m'"] = (
                        form[2:] if form.startswith("j'") else form
                    )  # pragma: no cover (subject key is usually "j'")
                else:
                    reflexive_forms[f"{subject} {pronoun}"] = form

        return {
            "infinitive": f"se {base_verb}",
            "base_verb": base_verb,
            "conjugation": reflexive_forms,
            "note": "Reflexive verbs always use être in compound tenses",
        }

    def subjunctive_practice(self, verb: str) -> dict[str, Union[str, dict[str, str], list[str]]]:
        """Practice subjunctive mood conjugation."""
        subj_forms = self.conjugate(verb, Tense.SUBJUNCTIVE_PRESENT)

        forms_dict = subj_forms.get("forms", {})
        example_form_1 = ""
        example_form_2 = ""

        if isinstance(forms_dict, dict):
            example_form_1 = forms_dict.get("que je", "parle")
            example_form_2 = forms_dict.get("qu'il/elle/on", "comprenne")

        return {
            "verb": verb,
            "forms": forms_dict,
            "trigger_phrases": [
                "Il faut que... - It's necessary that...",
                "Je veux que... - I want that...",
                "Il est important que... - It's important that...",
                "Bien que... - Although...",
                "Pour que... - So that...",
                "Avant que... - Before...",
                "J'ai peur que... - I'm afraid that...",
            ],
            "example_sentences": [
                f"Il faut que je {example_form_1}",
                f"Je veux qu'il {example_form_2}",
            ],
            "tip": "Subjunctive expresses doubt, emotion, necessity, or subjective thoughts",
        }
