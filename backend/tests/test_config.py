from app.core.config import Settings


def test_settings_defaults(monkeypatch):
    for name in (
        "APP_NAME",
        "REQUEST_TIMEOUT",
        "DEFAULT_LIMIT",
        "BAYESIAN_THRESHOLD",
    ):
        monkeypatch.delenv(name, raising=False)

    settings = Settings()

    assert settings.APP_NAME == "VSN Formula Brain"
    assert settings.REQUEST_TIMEOUT == 10
    assert settings.DEFAULT_LIMIT == 500
    assert settings.BAYESIAN_THRESHOLD == 0.65


def test_settings_reads_environment_values(monkeypatch):
    monkeypatch.setenv("APP_NAME", "Test VSN")
    monkeypatch.setenv("REQUEST_TIMEOUT", "30")
    monkeypatch.setenv("BAYESIAN_THRESHOLD", "0.8")

    settings = Settings()

    assert settings.APP_NAME == "Test VSN"
    assert settings.REQUEST_TIMEOUT == 30
    assert settings.BAYESIAN_THRESHOLD == 0.8
