from flask_sqlalchemy import SQLAlchemy
from models import *


def config_db(db:SQLAlchemy):
    # Configuração inicial do banco de dados
    # ROLE
    db.session.add(Role(name="Comum"))
    db.session.add(Role(name="Adminstrador"))
