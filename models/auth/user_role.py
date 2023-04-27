from models import db, User, Role


class UserRole(db.Model):
    __tablename__ = "users_roles"
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id_user), primary_key=True)
    id_role = db.Column(db.Integer(), db.ForeignKey(Role.id_role), primary_key=True)
