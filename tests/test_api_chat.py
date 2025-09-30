from fastapi.testclient import TestClient

from opengov_earlyfrench.api.main import app


def test_chat_endpoint_monkeypatched(monkeypatch) -> None:
    # Patch AI partner used by endpoint
    from opengov_earlyfrench.ai import conversation as conv_mod

    class FakeResp:
        french = "Bonjour !"
        english = "Hello!"
        grammar_notes = []
        vocabulary = []
        cultural_tips = []
        corrections = []
        pronunciation_tips = []
        follow_up = ""

    def fake_init(self, level="A1"):
        pass

    def fake_chat(self, msg):  # type: ignore[no-untyped-def]
        return FakeResp()

    monkeypatch.setattr(conv_mod.AIConversationPartner, "__init__", fake_init)
    monkeypatch.setattr(conv_mod.AIConversationPartner, "chat", fake_chat)

    client = TestClient(app)
    r = client.post("/api/v1/conversation/chat", json={"message": "salut", "level": "A1"})
    assert r.status_code == 200
    data = r.json()
    assert data["french"].startswith("Bonjour")
