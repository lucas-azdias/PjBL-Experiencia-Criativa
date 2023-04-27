from models import db, User


class Payment(db.Model):
    __tablename__ = "payments"
    id_payment = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id_user))
    value = db.Column(db.Float(), nullable=False)
    month = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    is_paid = db.Column(db.Boolean(), nullable=False)

    # Cópia do cartão usado
    card_num_card = db.Column(db.String(16), nullable=False)
    card_name_owner = db.Column(db.String(50), nullable=False)
    card_cvv = db.Column(db.String(3), nullable=False)
    card_month_expire_date = db.Column(db.Integer(), nullable=False)
    card_year_expire_date = db.Column(db.Integer(), nullable=False)
