from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from models import User


auth = Blueprint("auth", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@auth.route("/")
def auth_index():
    if not current_user.is_authenticated:
        return render_template("/auth/auth_index.html")
    else:
        return redirect(url_for("index"))


@auth.route("/login", methods=["POST"])
def auth_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.verify_password(password):
        return redirect(url_for("auth.auth_index"))
    
    login_user(user)

    if user.is_admin:
        return redirect(url_for("auth.auth_users_manager"))
    else:
        return redirect(url_for("index"))


@auth.route("/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("auth.auth_index"))
    

@auth.route("/register_user")
def auth_register_user():
    if not current_user.is_authenticated:
        return render_template("/auth/auth_register_user.html")
    else:
        return redirect(url_for("index"))


@auth.route("/users_manager")
@login_required
def auth_users_manager():
    if current_user.is_admin:
        users = User.query.all()
        usernames = [user.username for user in users]
        is_admin = [user.is_admin for user in users]
        return render_template("/auth/auth_users_manager.html", usernames=usernames, is_admin=is_admin)
    else:
        return redirect(url_for("index"))


@auth.route("/add_user", methods=["POST"])
def auth_add_user():
    username = request.form.get("username")
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    # Cartão de crédito
    card_num_card = request.form.get("card_num_card")
    card_name_owner = request.form.get("card_name_owner")
    card_cvv = request.form.get("card_cvv")
    card_expire_date = request.form.get("card_expire_date")
    
    card_expire_date = card_expire_date.split("-")
    card_month_expire_date = int(card_expire_date[0])
    card_year_expire_date = int(card_expire_date[1])


    is_admin = False
    if current_user.is_authenticated and current_user.is_admin:
        is_admin = True if request.form.get("is_admin") == "1" else False

    if None in [username, name, email, phone, password, confirm_password, is_admin, card_num_card, card_name_owner, card_cvv, card_expire_date]:
        return redirect(url_for(request.referrer))
    
    users = User.query.all()
    usernames = [user.username for user in users]

    if not username in usernames and password == confirm_password:
        user = User.insert_user(username, name, email, phone, password, is_admin, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date)
        if not current_user.is_authenticated:
            login_user(user)
    else:
        # Flash -> Erro - usuário já cadastrado
        if current_user.is_authenticated and current_user.is_admin:
            return redirect(url_for("auth.auth_users_manager"))
        else:
            return redirect(url_for("auth.auth_register_user"))
    
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for("auth.auth_users_manager"))
    else:
        return redirect(url_for("index"))
