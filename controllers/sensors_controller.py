from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from models import Sensor, User


sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@sensors.route('/')
def sensors_index():
    sensores = current_user.sensors
    return render_template("sensors/sensors_index.html", sensores=sensores, user=current_user)


@sensors.route('/list_sensors')
@login_required
def sensors_list_sensors():
    sensors = Sensor.get_sensors_by_id_user(current_user.id_user)
    resultado = request.form.get("choice")
    
    if(str(resultado) == "None"):
        return render_template("sensors/sensors_list_sensors.html", sensors=sensors)
    else:
        return render_template("sensors/sensors_list_sensors.html", sensors=sensors, resultado=resultado)


@sensors.route('/register_sensor')
@login_required
def sensors_register_sensor():
    return render_template("sensors/sensors_register_sensor.html")


@sensors.route('/add_sensor', methods=['POST'])
@login_required
def sensors_add_sensor():
    id_user = User.query.filter_by(username=current_user.username).first().id_user
    name = request.form.get("name")
    model = request.form.get("model")
    brand = request.form.get("brand")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")

    info = [id_user, name, model, brand, measure, voltage]

    if not None in info:
        Sensor.insert_sensor(*info)
        flash("Cadastrado com sucesso", "success")
        return redirect(url_for("sensors.sensors_list_sensors"))
    else:
        flash("Erro no cadastro", "danger")
        return redirect(url_for("sensors.sensors_add_sensor"))
