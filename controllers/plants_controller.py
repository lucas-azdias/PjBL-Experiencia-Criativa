from flask import Blueprint, render_template, redirect, url_for, request

from models import Sensor, Plant


plants = Blueprint("plants", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@plants.route('/')
def plants_index():
    plants = Plant.get_plants()
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
    if sensor is None:
        # lidar com erro, como redirecionar para página de erro ou retornar mensagem de erro
        return redirect(url_for("plants.plants_register_plant"))
    Plant.insert_plant(id_sensor, name, min_humidity)
    return redirect(url_for("plants.plants_index"))


''' 
@plants.route('/save_plant', methods=['POST'])

def plants_save_plant():
    plant_data = {
    'nome_planta': request.form.get("nome_planta"),
    'sensor': request.form.get("sensor"),
    'umidade': request.form.get("umidade")
    }
    global saved_plants
    saved_plants.append(plant_data)
    #saved_plants.append("Planta " + nome_planta + ", Sensor " + sensor + ", Umidade mínima " + umidade)
    return redirect(url_for("plants.plants_index"))
'''
