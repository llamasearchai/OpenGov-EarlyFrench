"""Configuration management for OpenGov-EarlyFrench."""

from functools import lru_cache
from typing import Union

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # API Configuration
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)
    api_prefix: str = Field(default="/api/v1")
    api_title: str = Field(default="OpenGov-EarlyFrench API")
    api_version: str = Field(default="0.1.0")

    # Security
    secret_key: SecretStr = Field(default=SecretStr("dev-secret-key"))
    jwt_secret: SecretStr = Field(default=SecretStr("dev-jwt-secret"))
    jwt_algorithm: str = Field(default="HS256")
    jwt_expiration_hours: int = Field(default=24)

    # AI Services
    openai_api_key: SecretStr = Field(default=SecretStr("sk-test"))
    openai_model: str = Field(default="gpt-4-turbo-preview")
    openai_temperature: float = Field(default=0.7)
    openai_max_tokens: int = Field(default=500)

    # French Variants
    default_french_variant: str = Field(default="metropolitan")
    supported_variants: list[str] = Field(
        default=["metropolitan", "quebec", "belgian", "swiss", "african"]
    )

    # Learning Settings
    srs_initial_interval: int = Field(default=1)
    srs_easy_multiplier: float = Field(default=2.5)
    srs_normal_multiplier: float = Field(default=2.0)
    srs_hard_multiplier: float = Field(default=1.3)
    srs_fail_multiplier: float = Field(default=0.5)

    max_daily_reviews: int = Field(default=100)
    max_daily_new_items: int = Field(default=20)
    session_time_limit: int = Field(default=60)

    min_accuracy_for_advancement: float = Field(default=0.8)
    streak_bonus_threshold: int = Field(default=7)

    # CEFR Levels
    cefr_levels: list[str] = Field(default=["A1", "A2", "B1", "B2", "C1", "C2"])

    # Content Settings
    enable_formal_informal: bool = Field(default=True)
    default_formality: str = Field(default="formal")
    enable_gender_patterns: bool = Field(default=True)
    enable_liaison_practice: bool = Field(default=True)
    enable_subjunctive_practice: bool = Field(default=True)

    # French-specific features
    nasal_vowels: list[str] = Field(default=["an", "en", "in", "on", "un"])
    accents: list[str] = Field(default=["aigu", "grave", "circonflexe", "tréma", "cédille"])

    # Gamification
    enable_gamification: bool = Field(default=True)
    xp_per_correct: int = Field(default=10)
    xp_per_streak_day: int = Field(default=50)
    achievement_system: bool = Field(default=True)

    # Logging
    log_level: str = Field(default="INFO")
    log_format: str = Field(default="json")
    enable_metrics: bool = Field(default=True)

    # CORS
    cors_origins: list[str] = Field(default=["http://localhost:3000", "http://localhost:8501"])

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: Union[str, list[str]]) -> list[str]:
        """Parse CORS origins."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
