from models import db


class Role(db.Model):
    __tablename__ = "roles"
    id_role = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # Relações N:N
    users = db.relationship("User", back_populates="roles", secondary="users_roles", lazy=True)
