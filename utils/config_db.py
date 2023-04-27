from flask import Flask

from models import *


def config_db(app:Flask):
    # Configuração inicial do banco de dados
    with app.app_context():
        # ROLE
        db.session.add(Role(name="Comum"))
        db.session.commit()
        db.session.add(Role(name="Adminstrador"))
        db.session.commit()
