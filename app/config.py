from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Telegram Bot Builder"
    APP_ENV: str = "development"

    BOT_BUILDER_TOKEN: str = ""

    DATABASE_URL: str = "sqlite:///telegram_builder.db"

    SECRET_KEY: str = ""
    JWT_SECRET_KEY: str = ""
    ENCRYPTION_KEY: str = ""

    ADMIN_EMAIL: str = ""
    ADMIN_PASSWORD: str = ""

    WEBHOOK_BASE_URL: str = ""

    TELEGRAM_API_BASE: str = "https://api.telegram.org"

    LOG_LEVEL: str = "INFO"

    KWIKUPI_API_KEY: str = ""
    KWIKUPI_API_SECRET: str = ""
    KWIKUPI_BASE_URL: str = "https://kwikupi.com/api"

    class Config:
        env_file = ".env"


settings = Settings()