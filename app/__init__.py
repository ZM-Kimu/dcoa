from flask import Flask

from app.models import dev_init
from app.modules.jwt import jwt
from app.modules.sql import db, migrate
from app.views import register_blueprints
from config.development import Config


def create_app() -> Flask:
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    jwt.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    dev_init(app)  # 数据库初始化操作，仅开发使用

    return app
