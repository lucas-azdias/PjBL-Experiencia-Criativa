from flask import Flask
from models import *


def create_db(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Configuração inicial do banco de dados
        # ROLE
        db.insert(Role).values(name="Comum")
        db.insert(Role).values(name="Adminstrador")
