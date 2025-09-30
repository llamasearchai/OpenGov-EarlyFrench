from opengov_earlyfrench.ai.conversation import AIConversationPartner


def test_ai_conversation_fallback_no_client() -> None:
    partner = AIConversationPartner(level="A1")
    # Force no client to take offline path
    partner.client = None  # type: ignore[assignment]
    resp = partner.chat("Bonjour")
    assert isinstance(resp.french, str)
    assert resp.french
    # Offline message expected
    assert "pas disponible" in resp.french or "Pardon" in resp.french


def test_system_prompt_builds() -> None:
    partner = AIConversationPartner(level="A2")
    text = partner._build_system_prompt()  # type: ignore[attr-defined]
    assert "Your responses should" in text
