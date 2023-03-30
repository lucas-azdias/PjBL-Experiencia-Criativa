from flask import Blueprint, request, render_template, redirect, url_for

sensor = Blueprint("sensor", __name__, 
                          template_folder="./views/", 
                          static_folder="./static/", 
                          root_path="./")

@sensor.route('/')
def sensor():
    global saved_data 
    return render_template('data/form_data.html',saved_data = saved_data)

