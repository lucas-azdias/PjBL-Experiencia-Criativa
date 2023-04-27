from flask import Blueprint, render_template , request



sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

saved_sensors = ["Avenca" , "Bambu"]

sensorTable = {}

sensorTable["Avenca"] = " 15-03-2002 - 50% " , " 17-04-2002 - 33%", " 17-05-2002 - 51%", " 17-06-2002 - 97%"
sensorTable["Bambu"] = " 15-03-2002 - 88% " , " 17-04-2002 - 55%", " 17-05-2002 - 11%", " 17-06-2002 - 79%"

@sensors.route('/')
def index():
    return render_template("sensors/sensors_index.html" , saved_sensors = saved_sensors)


@sensors.route('/sensors_select' , methods=['POST' , 'GET'])
def select_sensor():
    resultado = request.form.get("escolha")
    if(str(resultado) == "None"):
        print("A SUA ESCOLHA NO FORM FOI(none version): " + str(resultado))
        return render_template("sensors/sensors_select.html" , saved_sensors = saved_sensors)
    else:
        hash_escolida = sensorTable[resultado]
        last_record = hash_escolida[0]
        print("A SUA ESCOLHA NO FORM FOI(not None version): " + str(resultado))
        return render_template("sensors/sensors_select.html" , saved_sensors = saved_sensors , sensorTable = sensorTable , resultado = resultado , last_record = last_record )
