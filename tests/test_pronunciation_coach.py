"""Test French pronunciation coaching module."""

import pytest

from opengov_earlyfrench.core.pronunciation_coach import PronunciationCoach


def test_pronunciation_coach_initialization(pronunciation_coach: PronunciationCoach) -> None:
    """Test pronunciation coach initialization."""
    assert len(pronunciation_coach.nasal_vowels) == 4
    assert "an" in pronunciation_coach.nasal_vowels
    assert "r" in pronunciation_coach.special_sounds


def test_nasal_vowels(pronunciation_coach: PronunciationCoach) -> None:
    """Test nasal vowel teaching."""
    lesson = pronunciation_coach.teach_nasal_vowels()

    assert "vowels" in lesson
    assert "practice_phrases" in lesson
    assert "tips" in lesson

    vowels = lesson["vowels"]
    assert isinstance(vowels, dict)
    an_vowel = vowels["an"]
    assert "ipa" in an_vowel
    assert an_vowel["ipa"] == "/ɑ̃/"


def test_liaison_practice(pronunciation_coach: PronunciationCoach) -> None:
    """Test liaison practice."""
    result = pronunciation_coach.practice_liaison("les amis")

    assert "pronunciation" in result
    assert result["pronunciation"] == "lay-zah-MEE"
    assert "rule" in result
    assert "type" in result


def test_liaison_unknown_phrase(pronunciation_coach: PronunciationCoach) -> None:
    """Test liaison with unknown phrase."""
    result = pronunciation_coach.practice_liaison("un autre phrase")

    assert "tip" in result
    assert "common_liaisons" in result


def test_pronunciation_analysis(pronunciation_coach: PronunciationCoach) -> None:
    """Test pronunciation analysis."""
    analysis = pronunciation_coach.analyze_pronunciation("Je voudrais un croissant")

    assert analysis.text == "Je voudrais un croissant"
    assert analysis.score >= 0 and analysis.score <= 100
    assert len(analysis.challenges) > 0
    assert len(analysis.improvements) > 0


def test_pronunciation_analysis_simple_text(pronunciation_coach: PronunciationCoach) -> None:
    """Test pronunciation analysis with simple text."""
    analysis = pronunciation_coach.analyze_pronunciation("chat")

    assert analysis.text == "chat"
    assert isinstance(analysis.score, float)
    assert isinstance(analysis.challenges, list)


def test_minimal_pairs(pronunciation_coach: PronunciationCoach) -> None:
    """Test minimal pairs retrieval."""
    pairs = pronunciation_coach.get_minimal_pairs()

    assert "u_vs_ou" in pairs
    assert "é_vs_è" in pairs
    assert "an_vs_on" in pairs

    u_vs_ou = pairs["u_vs_ou"]
    assert "pairs" in u_vs_ou
    assert "tip" in u_vs_ou
    assert len(u_vs_ou["pairs"]) > 0

