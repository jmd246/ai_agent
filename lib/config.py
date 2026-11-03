import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # define the environment variables
    openai_api_key: str
    # tell pydantic to read the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # instance of the settings class


settings = Settings()
