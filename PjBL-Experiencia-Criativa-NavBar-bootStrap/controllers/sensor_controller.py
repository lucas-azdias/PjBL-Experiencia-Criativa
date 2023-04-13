from flask import Blueprint, request, render_template, redirect, url_for



sensor = Blueprint("sensor", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@sensor.route('/')
def sensor_index():
    return render_template('sensor/sensor_index.html')
