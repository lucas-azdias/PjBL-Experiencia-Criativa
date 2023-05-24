from flask import Blueprint, render_template, redirect, url_for, request

from models import Sensor, Plant, db


plants = Blueprint("plants", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@plants.route('/')
def plants_index():
    plants = Plant.get_plants_joined().all()
    return render_template('plants/plants_index.html', plants=plants)


@plants.route('/register_plant')
def plants_register_plant():
    sensors = Sensor.get_sensors()
    return render_template('plants/plants_register_plant.html', sensors=sensors)


@plants.route('/save_plant', methods=['POST'])
def plants_save_plant():
    id_sensor = request.form.get("id_sensor")
    name = request.form.get("name")
    min_humidity = request.form.get("min_humidity")

    sensor = Sensor.get_sensor(id_sensor)

    if not sensor is None:
        # lidar com erro, como redirecionar para página de erro ou retornar mensagem de erro
        Plant.insert_plant(id_sensor, name, min_humidity)
        return redirect(url_for("plants.plants_index"))
    else:
        return redirect(url_for("plants.plants_register_plant"))


@plants.route('/<int:id_plant>')
def show_plant(id_plant):
    plant = Plant.query.get(id_plant)
    return render_template('plants/plants_update_plant.html', plant=plant)


