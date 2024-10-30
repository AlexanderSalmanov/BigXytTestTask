from settings.base import Config as BaseConfig
from envparse import env

from dataclasses import dataclass


@dataclass
class Config(BaseConfig):
    FLASK_ENV: str = env('FLASK_ENV', 'local')