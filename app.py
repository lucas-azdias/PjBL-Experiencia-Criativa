from flask import Flask, render_template

from controllers.auth_controller import auth
from controllers.data_controller import data

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(data, url_prefix="/data")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/grafico')
def grafico():
    return render_template("grafico.html")

if __name__ == "__main__":
    app.run(debug=True)
