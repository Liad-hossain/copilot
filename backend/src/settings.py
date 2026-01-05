import multiprocessing
from urllib.parse import quote_plus

from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "copilot"
    app_version: str = "1.0.0"
    debug: bool = False

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    worker_count: int = multiprocessing.cpu_count() * 2 + 1
    reload: bool = False

    # Database
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_name: str = "copilot"

    @property
    def database_url(self) -> AnyUrl:
        return AnyUrl.build(
            scheme="postgresql",
            username=self.db_user,
            password=quote_plus(self.db_password),
            host=self.db_host,
            port=self.db_port,
            path=self.db_name,
        )

    # Security (optional - uncomment if needed)
    # secret_key: str = "your-secret-key"
    # access_token_expire_minutes: int = 30


settings = Settings()
