"""Test French gender teaching module."""

from opengov_earlyfrench.core.gender_teacher import GenderTeacher


def test_gender_teacher_initialization(gender_teacher: GenderTeacher) -> None:
    """Test gender teacher initialization."""
    assert len(gender_teacher.masculine_patterns) > 0
    assert len(gender_teacher.feminine_patterns) > 0
    assert len(gender_teacher.exceptions) > 0
    assert len(gender_teacher.articles) > 0


def test_identify_feminine_pattern(gender_teacher: GenderTeacher) -> None:
    """Test identifying feminine gender pattern."""
    result = gender_teacher.identify_pattern("information")

    assert result["word"] == "information"
    assert result["likely_gender"] == "feminine"
    assert "tion" in str(result["rule"]).lower()
    assert result.get("reliability") == "100%"


def test_identify_masculine_pattern(gender_teacher: GenderTeacher) -> None:
    """Test identifying masculine gender pattern."""
    result = gender_teacher.identify_pattern("gouvernement")

    assert result["word"] == "gouvernement"
    assert result["likely_gender"] == "masculine"
    assert "ment" in str(result["rule"]).lower()


def test_identify_unknown_pattern(gender_teacher: GenderTeacher) -> None:
    """Test identifying word with no clear pattern."""
    result = gender_teacher.identify_pattern("chat")

    assert result["word"] == "chat"
    assert result["likely_gender"] == "unknown"
    assert "No clear pattern" in result["rule"]


def test_partitive_practice(gender_teacher: GenderTeacher) -> None:
    """Test partitive article practice."""
    result = gender_teacher.partitive_practice()

    assert "explanation" in result
    assert "forms" in result
    assert "examples" in result
    assert "rules" in result

    forms = result["forms"]
    assert isinstance(forms, dict)
    assert forms.get("masculine") == "du"
    assert forms.get("feminine") == "de la"


def test_contractions(gender_teacher: GenderTeacher) -> None:
    """Test article contractions."""
    result = gender_teacher.get_contractions()

    assert "rules" in result
    assert "examples" in result
    assert "tip" in result

    rules = result["rules"]
    assert isinstance(rules, dict)
    assert rules["à + le"] == "au"
    assert rules["à + les"] == "aux"
    assert rules["de + le"] == "du"
    assert rules["de + les"] == "des"


def test_agreement_practice(gender_teacher: GenderTeacher) -> None:
    """Test adjective agreement practice."""
    result = gender_teacher.practice_agreement()

    assert "rules" in result
    assert "examples" in result
    assert "special_cases" in result

    rules = result["rules"]
    assert isinstance(rules, dict)
    assert "basic" in rules
    assert "feminine" in rules


def test_feminine_ending_ite(gender_teacher: GenderTeacher) -> None:
    """Test feminine ending -ité pattern."""
    result = gender_teacher.identify_pattern("liberté")

    assert result["likely_gender"] == "feminine"
    assert (
        "ité" in str(result.get("rule", "")).lower()
        or "feminine" in str(result.get("rule", "")).lower()
    )


def test_masculine_ending_age(gender_teacher: GenderTeacher) -> None:
    """Test masculine ending -age pattern."""
    result = gender_teacher.identify_pattern("voyage")

    assert result["likely_gender"] == "masculine"
    assert (
        "age" in str(result.get("rule", "")).lower()
        or "masculine" in str(result.get("rule", "")).lower()
    )


def test_exception_detection(gender_teacher: GenderTeacher) -> None:
    """Test exception detection in patterns."""
    result = gender_teacher.identify_pattern("page")

    assert result["word"] == "page"
    assert result.get("is_exception") or result["likely_gender"] == "feminine"
