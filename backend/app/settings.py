from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Lumends AI Platform"
    VERSION: str = "0.0.1-alpha"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
