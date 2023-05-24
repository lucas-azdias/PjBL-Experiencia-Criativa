from models import db, Sensor

from datetime import datetime


class Record(db.Model):
    __tablename__ = "records"
    id_record = db.Column(db.Integer(), primary_key=True)
    id_sensor = db.Column(db.Integer(), db.ForeignKey(Sensor.id_sensor))
    value = db.Column(db.Float(), nullable=False)
    register_date = db.Column(db.DateTime(), nullable=False, default=datetime.now())


    def insert_record(id_sensor, value, register_date):
        record = Record(id_sensor=id_sensor, value=value, register_date=register_date)
        db.session.add(record)
        db.session.commit()
        return record
    

    def update_record(id_record, id_sensor=None, value=None, register_date=None):
        record = Record.get_record(id_record)
        if id_sensor:
            record.id_sensor = id_sensor
        if value:
            record.value = value
        if register_date:
            record.register_date = register_date
        db.session.commit()
        return record


    def get_record(id_record):
        record = Record.query.filter_by(id_record=id_record).first()
        return record


    def get_records():
        records = Record.query.all()
        return records
    

    def delete_record(id_record):
        record = Record.get_record(id_record)
        record.delete()
        db.session.commit()
