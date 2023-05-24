from models import db, User

from datetime import datetime


class Payment(db.Model):
    __tablename__ = "payments"
    id_payment = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id_user))
    value = db.Column(db.Float(), nullable=False)
    month = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    is_paid = db.Column(db.Boolean(), nullable=False)
    date_payment = db.Column(db.Date(), nullable=False, default=datetime.today())

    # Cópia do cartão usado
    card_num_card = db.Column(db.String(16), nullable=False)
    card_name_owner = db.Column(db.String(50), nullable=False)
    card_cvv = db.Column(db.String(3), nullable=False)
    card_month_expire_date = db.Column(db.Integer(), nullable=False)
    card_year_expire_date = db.Column(db.Integer(), nullable=False)


    def insert_payment(id_user, value, month, year, is_paid, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date):
        payment = Payment(id_user=id_user, value=value, month=month,
                          year=year, is_paid=is_paid, card_num_card=card_num_card,
                          card_name_owner=card_name_owner, card_cvv=card_cvv,
                          card_month_expire_date=card_month_expire_date,
                          card_year_expire_date=card_year_expire_date)
        db.session.add(payment)
        db.session.commit()
        return payment


    def get_payment(id_payment):
        payment = Payment.query.filter_by(id_payment=id_payment).first()
        return payment


    def get_payments():
        payments = Payment.query.all()
        return payments
