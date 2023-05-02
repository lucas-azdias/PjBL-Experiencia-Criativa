from flask import Blueprint, render_template , request
from flask_login import login_user, logout_user, login_required, current_user

from models import Sensor , User


sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

@sensors.route('/')
def index():
    sensores = Sensor.findSensors(current_user)

    print("resposta da query dos sensores"+str(sensores))

    return render_template("sensors/sensors_index.html" , sensores = sensores , user = current_user)


@sensors.route('/sensors_select' , methods=['POST' , 'GET'])
@login_required
def select_sensor():
    sensors = Sensor.findSensors(current_user)
    resultado = request.form.get("escolha")
    if(str(resultado) == "None"):
        return render_template("sensors/sensors_select.html" , sensors = sensors)
    else:
        return render_template("sensors/sensors_select.html" , sensors = sensors , resultado = resultado)

@sensors.route('/create_sensor' ,  methods=['POST' , 'GET'])
@login_required
def create_sensor():
    user = User.query.filter_by(username=current_user.username).first()
    name  = request.form.get("name")
    model = request.form.get("model")
    brand = request.form.get("brand")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    if(name):
        response = Sensor.insert_sensor(user , name , model , brand , measure , voltage)
        print("RESPOSTA DO INSERT: " + str(response) +"---" + str(user))
        if(not response):
            error = 1
            return render_template("sensors/create_sensor.html",error = error)
        else:
            error = 0
            return render_template("sensors/create_sensor.html",error = error)
    else:
        return render_template("sensors/create_sensor.html")
