from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from controllers.auth_controller import add_user
from controllers.payment_controller import add_payment

from models import User, Payment

from datetime import datetime


admin = Blueprint("admin", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@admin.route("/")
def admin_index():
    return redirect(url_for("index"))


@admin.route("/users_manager")
@login_required
def admin_users_manager():
    if current_user.is_admin:
        users = User.query.all()
        usernames = [user.username for user in users]
        is_admin = [user.is_admin for user in users]
        current_month_year = datetime.today().strftime("%Y-%m")
        return render_template("/auth/auth_users_manager.html", usernames=usernames, is_admin=is_admin, current_month_year=current_month_year)
    else:
        # Sem permissão necessária
        flash("Sem permissão necessária", "danger")
        return redirect(url_for("index"))


@admin.route("/add_user", methods=["POST"])
def admin_add_user():
    if not current_user.is_admin:
        # Sem permissão necessária
        flash("Sem permissão necessária", "danger")
        return redirect(url_for("index"))
    
    # Dados do usuário
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

    # Verifica se deve dar permissão de admin
    is_admin = True if request.form.get("is_admin") == "1" else False

    add_user(username, name, email, phone, password, confirm_password,
             is_admin, card_num_card, card_name_owner, card_cvv, card_expire_date)

    return redirect(request.referrer)


@admin.route("/payments_manager")
@login_required
def admin_payments_manager():
    if current_user.is_admin:
        users = User.query.all()
        current_month_year = datetime.today().strftime("%Y-%m")
        usernames_payments = [(user.username, Payment.query.filter_by(id_user=user.id_user).all()) for user in users]
        usernames_options = dict()
        for i in range(len(users)):
            usernames_options[users[i].username] = f"{users[i].name} ({users[i].username})"
        return render_template("/payment/payment_payments_manager.html", current_month_year=current_month_year, usernames_payments=usernames_payments, usernames_options=usernames_options)
    else:
        # Sem permissão necessária
        flash("Sem permissão necessária", "danger")
        return redirect(url_for("index"))


@admin.route("/add_payment", methods=["POST"])
@login_required
def admin_add_payment():
    if not current_user.is_admin:
        # Sem permissão necessária
        flash("Sem permissão necessária", "danger")
        return redirect(url_for("index"))

    username = request.form.get("username")
    date = request.form.get("date")

    add_payment(username, date)
    
    return redirect(request.referrer)
