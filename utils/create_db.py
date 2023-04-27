from flask import Flask
from models import *


def create_db(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Configuração inicial do banco de dados
        # ROLE
        db.session.add(Role(name="Comum"))
        db.session.add(Role(name="Adminstrador"))
