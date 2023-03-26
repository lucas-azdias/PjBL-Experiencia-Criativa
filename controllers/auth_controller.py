from flask import Blueprint, request, render_template, url_for


auth = Blueprint("auth", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


# DADOS PUXADOS DO BANCO DE DADOS
users = [("admin", "12345678"), ("roberto", "gomes"), ("bafome", "jesus")] # (username, password)


@auth.route("/")
def auth_index():
    return render_template("/auth/auth_index.html")


@auth.route("/login", methods=["POST"])
def auth_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if (username, password) in users:
        return url_for("index")
    else:
        return url_for("auth.auth_index")
