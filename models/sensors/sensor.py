from models import db, User

from datetime import datetime


class Sensor(db.Model):
    __tablename__ = "sensors"
    id_sensor = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id_user))
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False, default="")
    brand = db.Column(db.String(50), nullable=False, default="")
    measure = db.Column(db.String(20), nullable=False, default="")
    voltage = db.Column(db.Float(), nullable=False)
    register_date = db.Column(db.DateTime(), nullable=False, default=datetime.now())

    # Relações 1:N
    records = db.relationship("Record", backref="sensors", lazy=True)
    plants = db.relationship("Plant", backref="sensors", lazy=True)
