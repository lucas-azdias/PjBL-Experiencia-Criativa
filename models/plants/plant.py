from models import db, Sensor


class Plant(db.Model):
    __tablename__ = "plants"
    id_plant = db.Column(db.Integer(), primary_key=True)
    id_sensor = db.Column(db.Integer(), db.ForeignKey(Sensor.id_sensor))
    name = db.Column(db.String(50), nullable=False)
    min_humidity = db.Column(db.Float(), nullable=False)

    #sensors = db.relationship("Sensor",backref="plants",lazy=True)

    def insert_plant(id_plant, id_sensor, name, min_humidity):
        
        plant =  Plant(id_plant=id_plant,id_sensor=id_sensor,name=name,min_humidity=min_humidity)

        db.session.add(plant)
        db.session.commit()
        return plant

