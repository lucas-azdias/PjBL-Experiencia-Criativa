from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models import User, Payment

from datetime import datetime


payment = Blueprint("payment", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

MONTH_SIGNING_VALUE = 19.99


@payment.route("/")
@login_required
def payment_index():
    payments = Payment.query.filter_by(id_user=current_user.id_user).all()
    return render_template("/payment/payment_index.html", payments=payments)


@payment.route("/register_payment")
@login_required
def payment_register_payment():
    current_month_year = datetime.today().strftime("%Y-%m")
    return render_template("/payment/payment_register_payment.html", current_month_year=current_month_year)


@payment.route("/payments_manager")
@login_required
def payment_payments_manager():
    if current_user.is_admin:
        users = User.query.all()
        current_month_year = datetime.today().strftime("%Y-%m")
        usernames_payments = [(user.username, Payment.query.filter_by(id_user=user.id_user).all()) for user in users]
        usernames_options = dict()
        for i in range(len(users)):
            usernames_options[users[i].username] = users[i].username
        return render_template("/payment/payment_payments_manager.html", current_month_year=current_month_year, usernames_payments=usernames_payments, usernames_options=usernames_options)
    else:
        # Sem permissão necessária
        flash("Sem permissão necessária", "danger")
        return redirect(url_for("index"))


@payment.route("/add_payment", methods=["POST"])
@login_required
def payment_add_payment():
    username = request.form.get("username")
    date = request.form.get("date")
    value = MONTH_SIGNING_VALUE

    if not username:
        username = current_user.username

    date = date.split("-")
    try:
        date_month = int(date[0])
        date_year = int(date[1])
    except:
        date_month = None
        date_year = None

    # Verifica se há alguma informação vazia
    info = [username, date_month, date_year]
    if None in info or "" in info:
        # Informações inválidas
        flash("Informações inválidas", "danger")
        return redirect(request.referrer)

    # Se haver um usuário com esse username, adiciona o pagamento
    user = User.query.filter_by(username=username).first()
    if user:
        Payment.insert_payment(user.id_user, value, date_year, date_month, True, user.card_num_card,
                               user.card_name_owner, user.card_cvv, user.card_month_expire_date, user.card_year_expire_date)
        
        # Pagamento efetuado com sucesso
        flash("Pagamento efetuado com sucesso", "success")
    else:
        # Erro no pagamento
        flash("Erro no pagamento", "warning")
    
    return redirect(request.referrer)
