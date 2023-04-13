from flask import Blueprint, request, render_template, redirect, url_for


data = Blueprint("data", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


saved_data = []


@data.route('/')
def data_index():
    global saved_data 
    return render_template('data/data_form_data.html', saved_data=saved_data)


@data.route('/list_data')
def data_list_data():
    global saved_data
    return render_template('data/data_list_form_data.html', saved_data=saved_data)


@data.route('/get_data', methods = ['POST'])
def data_get_data():
    nome_planta = request.form.get("nome_planta")
    sensor = request.form.get("sensor")
    umidade = request.form.get("umidade")
    global saved_data 
    saved_data.append("Planta " + nome_planta + ", Sensor " + sensor + ", Umidade mínima " + umidade)
    return redirect(url_for("data.data_list_data"))
