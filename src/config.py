from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token:str = Field("BOT_TOKEN")
    default_node_name:str = Field("DEFAULT_NODE_NAME")
    node_id:str = Field("NODE_ID")
    node_ip:str = Field("NODE_IP")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
