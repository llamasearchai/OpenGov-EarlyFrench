"""Test French verb conjugation system."""

from opengov_earlyfrench.core.models import Tense
from opengov_earlyfrench.core.verb_conjugator import VerbConjugator


def test_regular_er_verb(verb_conjugator: VerbConjugator) -> None:
    """Test regular -er verb conjugation."""
    result = verb_conjugator.conjugate("parler", Tense.PRESENT)

    assert "forms" in result
    forms = result["forms"]
    assert isinstance(forms, dict)
    assert forms.get("je") == "parle" or forms.get("j'") == "parle"
    assert forms["tu"] == "parles"
    assert forms["il/elle/on"] == "parle"
    assert forms["nous"] == "parlons"
    assert forms["vous"] == "parlez"
    assert forms["ils/elles"] == "parlent"


def test_irregular_verb_etre(verb_conjugator: VerbConjugator) -> None:
    """Test irregular verb être conjugation."""
    result = verb_conjugator.conjugate("être", Tense.PRESENT)

    assert result.get("type") == "irregular"
    forms = result.get("forms", {})
    assert isinstance(forms, dict)
    assert forms["je"] == "suis"
    assert forms["tu"] == "es"
    assert forms["il/elle/on"] == "est"
    assert forms["nous"] == "sommes"


def test_irregular_verb_avoir(verb_conjugator: VerbConjugator) -> None:
    """Test irregular verb avoir conjugation."""
    result = verb_conjugator.conjugate("avoir", Tense.PRESENT)

    assert result.get("type") == "irregular"
    forms = result.get("forms", {})
    assert isinstance(forms, dict)
    assert forms["j'"] == "ai"
    assert forms["tu"] == "as"
    assert forms["il/elle/on"] == "a"


def test_irregular_verb_aller(verb_conjugator: VerbConjugator) -> None:
    """Test irregular verb aller conjugation."""
    result = verb_conjugator.conjugate("aller", Tense.PRESENT)

    forms = result.get("forms", {})
    assert isinstance(forms, dict)
    assert forms["je"] == "vais"
    assert forms["tu"] == "vas"
    assert forms["il/elle/on"] == "va"
    assert forms["nous"] == "allons"


def test_passe_compose_formation(verb_conjugator: VerbConjugator) -> None:
    """Test passé composé formation."""
    result = verb_conjugator.form_passe_compose("parler", "je")

    assert result["auxiliary"] == "avoir"
    assert "ai" in str(result["auxiliary_form"]).lower()
    assert result["past_participle"] == "parlé"
    assert "parlé" in str(result["complete_form"])


def test_passe_compose_etre_verb(verb_conjugator: VerbConjugator) -> None:
    """Test passé composé with être auxiliary."""
    result = verb_conjugator.form_passe_compose("aller", "je")

    assert result["auxiliary"] == "être"
    assert result["past_participle"] == "allé"


def test_reflexive_verb(verb_conjugator: VerbConjugator) -> None:
    """Test reflexive verb conjugation."""
    result = verb_conjugator.reflexive_verb("se lever")

    assert "conjugation" in result
    assert "base_verb" in result
    assert result["base_verb"] == "lever"
    assert result["note"] == "Reflexive verbs always use être in compound tenses"

    conjugation = result["conjugation"]
    assert isinstance(conjugation, dict)
    assert any("je" in key for key in conjugation)


def test_subjunctive_practice(verb_conjugator: VerbConjugator) -> None:
    """Test subjunctive practice."""
    result = verb_conjugator.subjunctive_practice("être")

    assert "verb" in result
    assert result["verb"] == "être"
    assert "forms" in result
    assert "trigger_phrases" in result
    assert "tip" in result

    triggers = result["trigger_phrases"]
    assert isinstance(triggers, list)
    assert len(triggers) > 0


def test_conjugate_with_subject(verb_conjugator: VerbConjugator) -> None:
    """Test conjugation with specific subject."""
    result = verb_conjugator.conjugate("être", Tense.PRESENT, "je")

    assert "subject" in result
    assert result["subject"] == "je"
    assert "form" in result
    assert result["form"] == "suis"


def test_imparfait_conjugation(verb_conjugator: VerbConjugator) -> None:
    """Test imparfait tense conjugation."""
    result = verb_conjugator.conjugate("parler", Tense.IMPARFAIT)

    forms = result.get("forms", {})
    assert isinstance(forms, dict)
    assert any("ais" in form for form in forms.values())


def test_futur_simple_conjugation(verb_conjugator: VerbConjugator) -> None:
    """Test futur simple tense conjugation."""
    result = verb_conjugator.conjugate("parler", Tense.FUTUR_SIMPLE)

    forms = result.get("forms", {})
    assert isinstance(forms, dict)
    assert any("erai" in form or "rai" in form for form in forms.values())
