"""Test FastAPI endpoints."""

from fastapi.testclient import TestClient


def test_root_endpoint(api_client: TestClient) -> None:
    """Test root endpoint."""
    response = api_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_health_endpoint(api_client: TestClient) -> None:
    """Test health check endpoint."""
    response = api_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_analyze_pronunciation(api_client: TestClient) -> None:
    """Test pronunciation analysis endpoint."""
    response = api_client.post(
        "/api/v1/pronunciation/analyze", json={"text": "Je voudrais un croissant"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "score" in data
    assert "challenges" in data
    assert "improvements" in data


def test_nasal_vowels_endpoint(api_client: TestClient) -> None:
    """Test nasal vowels teaching endpoint."""
    response = api_client.get("/api/v1/pronunciation/nasal-vowels")
    assert response.status_code == 200
    data = response.json()
    assert "explanation" in data
    assert "vowels" in data


def test_liaison_practice_endpoint(api_client: TestClient) -> None:
    """Test liaison practice endpoint."""
    response = api_client.get("/api/v1/pronunciation/liaison/les amis")
    assert response.status_code == 200
    data = response.json()
    assert "phrase" in data


def test_minimal_pairs_endpoint(api_client: TestClient) -> None:
    """Test minimal pairs endpoint."""
    response = api_client.get("/api/v1/pronunciation/minimal-pairs")
    assert response.status_code == 200
    data = response.json()
    assert "u_vs_ou" in data


def test_conjugate_verb_endpoint(api_client: TestClient) -> None:
    """Test verb conjugation endpoint."""
    response = api_client.post(
        "/api/v1/verbs/conjugate", json={"verb": "parler", "tense": "présent"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "forms" in data or "error" in data


def test_passe_compose_endpoint(api_client: TestClient) -> None:
    """Test passé composé endpoint."""
    response = api_client.get("/api/v1/verbs/parler/passe-compose/je")
    assert response.status_code == 200
    data = response.json()
    assert "auxiliary" in data
    assert "past_participle" in data


def test_reflexive_verb_endpoint(api_client: TestClient) -> None:
    """Test reflexive verb endpoint."""
    response = api_client.get("/api/v1/verbs/se lever/reflexive")
    assert response.status_code == 200
    data = response.json()
    assert "conjugation" in data


def test_subjunctive_endpoint(api_client: TestClient) -> None:
    """Test subjunctive practice endpoint."""
    response = api_client.get("/api/v1/verbs/être/subjunctive")
    assert response.status_code == 200
    data = response.json()
    assert "verb" in data
    assert "trigger_phrases" in data


def test_identify_gender_endpoint(api_client: TestClient) -> None:
    """Test gender identification endpoint."""
    response = api_client.post("/api/v1/gender/identify", json={"word": "information"})
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert "likely_gender" in data


def test_partitive_endpoint(api_client: TestClient) -> None:
    """Test partitive practice endpoint."""
    response = api_client.get("/api/v1/gender/partitive")
    assert response.status_code == 200
    data = response.json()
    assert "explanation" in data
    assert "forms" in data


def test_contractions_endpoint(api_client: TestClient) -> None:
    """Test contractions endpoint."""
    response = api_client.get("/api/v1/gender/contractions")
    assert response.status_code == 200
    data = response.json()
    assert "rules" in data


def test_agreement_endpoint(api_client: TestClient) -> None:
    """Test agreement practice endpoint."""
    response = api_client.get("/api/v1/gender/agreement")
    assert response.status_code == 200
    data = response.json()
    assert "rules" in data
    assert "examples" in data


def test_scenario_endpoint(api_client: TestClient) -> None:
    """Test conversation scenario endpoint."""
    response = api_client.get("/api/v1/conversation/scenario/café")
    assert response.status_code == 200
    data = response.json()
    assert "dialogue" in data
    assert "vocabulary" in data
