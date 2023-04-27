from models import db


class User(db.Model):
    __tablename__ = "users"
    id_user = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(512), nullable=False)

    # Cartão de crédito
    card_num_card = db.Column(db.String(16), nullable=False)
    card_name_owner = db.Column(db.String(50), nullable=False)
    card_cvv = db.Column(db.String(3), nullable=False)
    card_month_expire_date = db.Column(db.Integer(), nullable=False)
    card_year_expire_date = db.Column(db.Integer(), nullable=False)

    # Relações N:N
    roles = db.relationship("Role", back_populates="users", secondary="users_roles", lazy=True)

    # Relações 1:N
    payments = db.relationship("Payment", backref="users", lazy=True)
