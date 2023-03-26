from flask import Flask, render_template

from controllers.auth_controller import auth


app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(auth, url_prefix="/auth")


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
