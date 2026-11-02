from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "NTUMBA TRADER"
    environment: str = "development"
    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.vercel.app",
    ]


settings = Settings()
