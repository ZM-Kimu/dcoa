import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()


class Config:
    STATIC_FOLDER = "public"
    STATIC_URL_PATH = "/static"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=5)

    SECRET_KEY = os.getenv("SECRET_KEY")  # 加载 SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用警告
