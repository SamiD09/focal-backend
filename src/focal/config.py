from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = '.env',
        env_file_encoding = 'utf-8',
        extra = 'ignore',
    )
    
    environment : str = 'development'
    cors_origins : str ='http://localhost:5173'
    firebase_credentials_path: str = 'firebase-key.json'
    
    @property
    def cors_origin_list(self) -> list[str]:
        return  [o.strip().rstrip("/") for o in self.cors_origins.split(",") if o.strip()]
    
@lru_cache
def get_settings() -> Settings:
    return Settings()
