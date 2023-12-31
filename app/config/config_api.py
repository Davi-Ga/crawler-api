import os

from starlette.config import Config

config = Config(".env")

API_PREFIX = config("API_PREFIX", cast=str,default="/api")
DEBUG = config("DEBUG", cast=bool,default=True)
PROJECT_NAME = config("PROJECT_NAME", cast=str,default="Jurisprudence Crawler")
VERSION = config("VERSION", cast=str,default="1.0.0")

EMAIL = config("EMAIL", cast=str,default="email")
PASSWORD = config("PASSWORD", cast=str,default="password")

