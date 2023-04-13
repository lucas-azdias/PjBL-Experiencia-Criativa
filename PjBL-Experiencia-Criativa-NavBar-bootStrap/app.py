from flask import Flask, render_template

from controllers.auth_controller import auth
from controllers.data_controller import data
from controllers.sensor_controller import sensor


app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(sensor, url_prefix="/sensor")


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
