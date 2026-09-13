from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Garimpeiro PCW"
    database_url: str = "sqlite:///./garimpeiro.db"
    scrape_enabled: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
