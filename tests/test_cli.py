from typer.testing import CliRunner

from opengov_earlyfrench.cli import app


runner = CliRunner()


def test_cli_version() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "OpenGov-EarlyFrench version" in result.stdout


def test_cli_pronunciation_commands() -> None:
    # Nasal lesson
    res1 = runner.invoke(app, ["pronunciation", "--nasal"])  # type: ignore[list-item]
    assert res1.exit_code == 0
    assert "Nasal Vowels Lesson" in res1.stdout

    # Liaison
    res2 = runner.invoke(app, ["pronunciation", "--liaison", "les amis"])  # type: ignore[list-item]
    assert res2.exit_code == 0
    assert "Liaison Practice" in res2.stdout

    # Liaison unknown phrase branch
    res2b = runner.invoke(app, ["pronunciation", "--liaison", "foo bar"])  # type: ignore[list-item]
    assert res2b.exit_code == 0
    assert "Check if there's a consonant before a vowel sound" in res2b.stdout

    # Analysis
    res3 = runner.invoke(app, ["pronunciation", "--text", "Je parle un peu français"])  # type: ignore[list-item]
    assert res3.exit_code == 0
    assert "Pronunciation Analysis" in res3.stdout

    # No flags usage message
    res4 = runner.invoke(app, ["pronunciation"])  # type: ignore[list-item]
    assert res4.exit_code == 0
    assert "Use --text, --nasal, or --liaison" in res4.stdout


def test_cli_conjugate_commands() -> None:
    # Regular verb
    r1 = runner.invoke(app, ["conjugate", "parler", "--tense", "présent"])  # type: ignore[list-item]
    assert r1.exit_code == 0
    assert "Conjugation: parler" in r1.stdout

    # Irregular verb
    r2 = runner.invoke(app, ["conjugate", "être", "--tense", "présent"])  # type: ignore[list-item]
    assert r2.exit_code == 0
    assert "Conjugation: être" in r2.stdout

    # Reflexive verb
    r3 = runner.invoke(app, ["conjugate", "se lever", "--reflexive"])  # type: ignore[list-item]
    assert r3.exit_code == 0
    assert "Reflexive Verb" in r3.stdout

    # Subjunctive practice
    r4 = runner.invoke(app, ["conjugate", "être", "--subjunctive"])  # type: ignore[list-item]
    assert r4.exit_code == 0
    assert "Subjunctive Practice" in r4.stdout

    # Third-group future (no forms available) renders empty table without error
    r5 = runner.invoke(app, ["conjugate", "prendre", "--tense", "futur_simple"])  # type: ignore[list-item]
    assert r5.exit_code == 0


def test_cli_gender_commands() -> None:
    # Contractions
    g1 = runner.invoke(app, ["gender", "information", "--contractions"])  # type: ignore[list-item]
    assert g1.exit_code == 0
    assert "Article Contractions" in g1.stdout

    # Partitive
    g2 = runner.invoke(app, ["gender", "pain", "--partitive"])  # type: ignore[list-item]
    assert g2.exit_code == 0
    assert "Partitive Articles Practice" in g2.stdout

    # Identify
    g3 = runner.invoke(app, ["gender", "nation"])  # type: ignore[list-item]
    assert g3.exit_code == 0
    assert "Gender Analysis" in g3.stdout

    # Masculine
    g4 = runner.invoke(app, ["gender", "fromage"])  # type: ignore[list-item]
    assert g4.exit_code == 0
    assert "Masculine" in g4.stdout

    # Unknown
    g5 = runner.invoke(app, ["gender", "xyz"])  # type: ignore[list-item]
    assert g5.exit_code == 0
    assert "Unknown" in g5.stdout

    # Exception warning path
    g6 = runner.invoke(app, ["gender", "page"])  # type: ignore[list-item]
    assert g6.exit_code == 0
    assert "Warning" in g6.stdout


def test_cli_scenario() -> None:
    s = runner.invoke(app, ["scenario", "café"])  # type: ignore[list-item]
    assert s.exit_code == 0
    assert "Scenario:" in s.stdout


def test_cli_chat_quick_exit(monkeypatch) -> None:
    # Mock AI partner to avoid network and produce contentful response
    import opengov_earlyfrench.cli as cli_mod

    class FakeResp:
        french = "Salut !"
        english = "Hi!"
        grammar_notes = ["présent"]
        vocabulary = ["salut", "bonjour", "merci"]
        cultural_tips = ["Always greet politely"]

    def fake_init(self, level="A1"):
        pass

    def fake_chat(self, text):  # type: ignore[no-untyped-def]
        return FakeResp()

    monkeypatch.setattr(cli_mod.AIConversationPartner, "__init__", fake_init)
    monkeypatch.setattr(cli_mod.AIConversationPartner, "chat", fake_chat)

    # Provide a message then exit to exercise printing paths
    result = runner.invoke(app, ["chat"], input="bonjour\nexit\n")
    assert result.exit_code == 0
    assert "[AI]" in result.stdout


def test_cli_serve_monkeypatched(monkeypatch) -> None:
    # Mock uvicorn.run to avoid starting server
    calls = {}

    def fake_run(*args, **kwargs):  # type: ignore[no-untyped-def]
        calls["called"] = True
        calls["args"] = args
        calls["kwargs"] = kwargs

    import uvicorn  # type: ignore

    monkeypatch.setattr(uvicorn, "run", fake_run)
    res = runner.invoke(app, ["serve", "--host", "127.0.0.1", "--port", "1234"])  # type: ignore[list-item]
    assert res.exit_code == 0
    assert calls.get("called") is True
