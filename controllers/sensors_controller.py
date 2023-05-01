from flask import Blueprint, render_template , request
from flask_login import login_user, logout_user, login_required, current_user

from models import Sensor , User


sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

user = current_user

saved_sensors = ["Avenca" , "Bambu"]

sensorTable = {}

sensorTable["Avenca"] = " 15-03-2002 - 50% " , " 17-04-2002 - 33%", " 17-05-2002 - 51%", " 17-06-2002 - 97%"
sensorTable["Bambu"] = " 15-03-2002 - 88% " , " 17-04-2002 - 55%", " 17-05-2002 - 11%", " 17-06-2002 - 79%"

@sensors.route('/')
def index():
    sensores = Sensor.query.all()
    return render_template("sensors/sensors_index.html" , saved_sensors = sensores , user = user.username)


@sensors.route('/sensors_select' , methods=['POST' , 'GET'])
def select_sensor():
    name = user.username
    resultado = request.form.get("escolha")
    sensores = User.query.filter_by(name=resultado).first()
    print("RESPOSTA DO FILTRO DE SENSORES: "+ str(sensores))
    if(str(resultado) == "None"):
        print("A SUA ESCOLHA NO FORM FOI(none version): " + str(resultado))
        return render_template("sensors/sensors_select.html" , saved_sensors = sensores)
    else:
        hash_escolida = sensorTable[resultado]
        last_record = hash_escolida[0]
        print("A SUA ESCOLHA NO FORM FOI(not None version): " + str(resultado))
        return render_template("sensors/sensors_select.html" , saved_sensors = sensores , sensorTable = sensorTable , resultado = resultado , last_record = last_record )

@sensors.route('/create_sensor' ,  methods=['POST' , 'GET'])
def create_sensor():
    user = User.query.filter_by(username=current_user.username).first()
    name  = request.form.get("name")
    model = request.form.get("model")
    brand = request.form.get("brand")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    if(name):
        response = Sensor.insert(user , name , model , brand , measure , voltage)
        print("RESPOSTA DO INSERT: " + str(response) +"---" + str(user))
        if(not response):
            error = 1
            return render_template("sensors/create_sensor.html",error = error)
        else:
            error = 0
            return render_template("sensors/create_sensor.html",error = error)
    else:
        return render_template("sensors/create_sensor.html")
