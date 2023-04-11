from flask import Blueprint, request, render_template, redirect, url_for


payment = Blueprint("payment", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


# DADOS PUXADOS DO BANCO DE DADOS
users = ["admin", "roberto", "bafome"] # username
cards = dict() # "username": ((name_card, id_card, exp_date, cvv), ...)


@payment.route("/")
def payment_index():
    return render_template("/payment/payment_index.html")


@payment.route("/list_data")
def payment_list_data():
    return render_template("/payment/payment_list_card.html", cards=cards)


@payment.route("/register_card", methods=["POST"])
def payment_register_card():
    username = request.form.get("username")
    name_card = request.form.get("name_card")
    id_card = request.form.get("id_card")
    exp_date = request.form.get("exp_date")
    cvv = request.form.get("cvv")

    if username != "" and name_card != "" and id_card != "" and exp_date != "" and cvv != "":
        if not username in cards.keys():
            cards[username] = list()
        cards[username].append((name_card, id_card, exp_date, cvv))
        return url_for("payment.payment_list_data")
    else:
        return url_for("payment.payment_index")
