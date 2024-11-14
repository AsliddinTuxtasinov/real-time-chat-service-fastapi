import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'real-time-chat-service'
    APP_VERSION: str = '0.0.1'
    APP_DESCRIPTION: str = 'Real-time chat Service'
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str
    DATABASE_URL: str  # The URL format is: "postgresql+psycopg2://username:password@host:port/database_name"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
