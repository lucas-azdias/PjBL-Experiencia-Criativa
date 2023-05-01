from models import db
from models.sensors.sensor import Sensor

class Plant(db.Model):
    __tablename__ = "plants"
    id_plant = db.Column(db.Integer(), primary_key=True)
    id_sensor = db.Column(db.Integer(), db.ForeignKey(Sensor.id_sensor))
    name = db.Column(db.String(50), nullable=False)
    min_humidity = db.Column(db.Float(), nullable=False)
