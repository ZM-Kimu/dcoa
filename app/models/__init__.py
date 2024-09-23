from flask import Flask
from flask_migrate import revision, upgrade

from app.utils.constant import DataStructure as D
from app.utils.database import CRUD

from . import department, verification
from .member import Member


def dev_init(app: Flask) -> None:
    try:
        with app.app_context():
            upgrade(revision="head")  # 更新db结构
            revision(message="init", autogenerate=True)
            print("DB initialized.")

            with CRUD(
                Member,
                id="2021400122",
                name="root",
                major="empty",
                role=D.admin,
                learning="None",
            ) as i:
                if not i.query_key():
                    i.add()
                    i.instance.set_password()

    except Exception as e:
        raise RuntimeError(f"Failed to initialize the db: {e}")
