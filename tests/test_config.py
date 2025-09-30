from opengov_earlyfrench.config import Settings


def test_cors_origins_parsing_from_string_value() -> None:
    s = Settings(cors_origins="http://a,http://b")
    assert s.cors_origins == ["http://a", "http://b"]
