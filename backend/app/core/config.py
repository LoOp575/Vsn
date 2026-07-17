import os
from dataclasses import dataclass, field

from dotenv import load_dotenv


load_dotenv()


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    return int(value) if value is not None else default


def _env_float(name: str, default: float) -> float:
    value = os.getenv(name)
    return float(value) if value is not None else default


def _env_str(name: str, default: str) -> str:
    return os.getenv(name, default)


@dataclass(frozen=True)
class Settings:
    APP_NAME: str = field(default_factory=lambda: _env_str("APP_NAME", "VSN Formula Brain"))
    APP_VERSION: str = field(default_factory=lambda: _env_str("APP_VERSION", "0.1.0"))

    MEXC_BASE_URL: str = field(
        default_factory=lambda: _env_str("MEXC_BASE_URL", "https://api.mexc.com")
    )
    REQUEST_TIMEOUT: int = field(default_factory=lambda: _env_int("REQUEST_TIMEOUT", 10))

    DEFAULT_INTERVAL: str = field(default_factory=lambda: _env_str("DEFAULT_INTERVAL", "1m"))
    DEFAULT_LIMIT: int = field(default_factory=lambda: _env_int("DEFAULT_LIMIT", 500))
    MAX_GAINERS: int = field(default_factory=lambda: _env_int("MAX_GAINERS", 50))

    MONTE_CARLO_PATHS: int = field(default_factory=lambda: _env_int("MONTE_CARLO_PATHS", 1000))
    BAYESIAN_THRESHOLD: float = field(default_factory=lambda: _env_float("BAYESIAN_THRESHOLD", 0.65))


settings = Settings()
