from flask import Blueprint, request, render_template, redirect, url_for
from json import dumps


auth = Blueprint("auth", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


# DADOS PUXADOS DO BANCO DE DADOS
users = [("admin", "12345678", True), ("roberto", "gomes", False), ("bafome", "jesus", True)] # (username, password, is_admin)

isLogged = False
isAdmin = False


@auth.route("/")
def auth_index():
    global isLogged, isAdmin
    isLogged = False
    isAdmin = False
    return render_template("/auth/auth_index.html")


@auth.route("/login", methods=["POST"])
def auth_login():
    username = request.form.get("username")
    password = request.form.get("password")

    ifAdmin = (username, password, True) in users
    ifComum = (username, password, False) in users

    global isLogged, isAdmin
    if ifAdmin or ifComum:
        isLogged = True
        if ifAdmin:
            isAdmin = True
            return url_for("auth.auth_users_manager")
        else:
            isAdmin = False
            return url_for("index")
    else:
        isLogged = False
        isAdmin = False
        return url_for("auth.auth_index")


@auth.route("/users_manager")
def auth_users_manager():
    if isLogged and isAdmin:
        usernames = [user[0] for user in users]
        is_admin = [user[2] for user in users]
        return render_template("/auth/auth_users_manager.html", usernames=usernames, is_admin=is_admin)
    elif isLogged and not isAdmin:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("auth.auth_index"))


@auth.route("/get_usernames", methods=["POST"])
def auth_get_usernames():
    if isLogged and isAdmin:
        usernames = [user[0] for user in users]
        return dumps(usernames)
    elif isLogged and not isAdmin:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("auth.auth_index"))


@auth.route("/add_user", methods=["POST"])
def auth_add_user():
    if isLogged and isAdmin:
        username = request.form.get("username")
        password = request.form.get("password")
        is_admin = int(request.form.get("is_admin"))

        user = (username, password, True if is_admin == 1 else False)
        if not user in users:
            users.append(user)
        return url_for("auth.auth_users_manager")
    elif isLogged and not isAdmin:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("auth.auth_index"))
