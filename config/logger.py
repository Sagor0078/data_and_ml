import os
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

class LoggerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    log_level: str

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def configure_logging(log_level: str) -> None:
    logger.remove() 
    logger.add(
        f'{log_dir}/app.log',
        rotation='1 day',  
        retention='2 days',  
        compression='zip',  
        level=log_level,  
    )

configure_logging(log_level=LoggerSettings().log_level)
