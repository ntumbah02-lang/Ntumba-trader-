from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "NTUMBA TRADER"
    environment: str = "development"
    secret_key: str = "demo-secret-key-change-me"
    api_v1_prefix: str = "/api"
    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.vercel.app",
    ]
    database_url: str = "sqlite:///./ntumba_trader.db"
    access_token_expire_minutes: int = 60


settings = Settings()
