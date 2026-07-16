from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "VSN Formula Brain"
    APP_VERSION: str = "0.1.0"

    MEXC_BASE_URL: str = "https://api.mexc.com"
    REQUEST_TIMEOUT: int = 10

    DEFAULT_INTERVAL: str = "1m"
    DEFAULT_LIMIT: int = 500
    MAX_GAINERS: int = 50

    MONTE_CARLO_PATHS: int = 1000
    BAYESIAN_THRESHOLD: float = 0.65

    class Config:
        env_file = ".env"

settings = Settings()
