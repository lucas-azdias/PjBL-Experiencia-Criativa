from models import db, Sensor


class Plant(db.Model):
    __tablename__ = "plants"
    id_plant = db.Column(db.Integer(), primary_key=True)
    id_sensor = db.Column(db.Integer(), db.ForeignKey(Sensor.id_sensor))
    name = db.Column(db.String(50), nullable=False)
    min_humidity = db.Column(db.Float(), nullable=False)


    def insert_plant(id_sensor, name, min_humidity):
        plant =  Plant(id_sensor=id_sensor, name=name,
                       min_humidity=min_humidity)
        db.session.add(plant)
        db.session.commit()
        return plant
    

    def select_plant():
        select_plants = Plant.query.all()
        return select_plants
