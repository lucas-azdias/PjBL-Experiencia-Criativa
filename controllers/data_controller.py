from flask import Blueprint, request, render_template, redirect, url_for

data = Blueprint("data", __name__, 
                          template_folder="./views/", 
                          static_folder="./static/", 
                          root_path="./")

saved_data = []

@data.route('/')
def data_index():
    global saved_data 
    return render_template('data/form_data.html',saved_data = saved_data)


@data.route('/list_data')
def list_data():
    global saved_data
    return render_template('data/list_form_data.html',saved_data = saved_data)

@data.route('/form_data')
def form_data():
     return render_template('data/form_data.html', saved_data = saved_data)


@data.route('/get_data', methods = ['POST'])
def get_data():
    nome_planta = request.form.get("nome_planta",None)
    sensor_utilizado = request.form.get("sensor",None)
    global saved_data 
    saved_data.append(nome_planta+","+sensor_utilizado)
    return redirect(url_for("data.list_data"))
