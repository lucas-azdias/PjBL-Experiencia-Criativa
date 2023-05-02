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

    
    def insert_sensor(user , name, model , brand , measure , voltage):
        
        sensor = Sensor(id_user=user.id_user,name=name,model=model,brand=brand ,measure= measure,voltage=voltage)

        db.session.add(sensor)
        db.session.commit()
        return 1

    def findSensors(user):
        user = User.query.filter_by(id_user=user.id_user).first()
        user_sensors = user.sensors
        return user_sensors
    