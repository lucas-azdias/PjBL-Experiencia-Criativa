from models import db, login_manager


class User(db.Model):
    __tablename__ = "users"
    id_user = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(512), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)

    # Cartão de crédito
    card_num_card = db.Column(db.String(16), nullable=False)
    card_name_owner = db.Column(db.String(50), nullable=False)
    card_cvv = db.Column(db.String(3), nullable=False)
    card_month_expire_date = db.Column(db.Integer(), nullable=False)
    card_year_expire_date = db.Column(db.Integer(), nullable=False)

    # Relações 1:N
    payments = db.relationship("Payment", backref="users", lazy=True)

    # Métodos necessários para o Flask-Login
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    # User-loader do Flask-Login
    @login_manager.user_loader
    def get_user(id_user):
        return User.query.filter_by(id_user=id_user).first()


    def get_id(self):
        return str(self.id_user)
    

    def verify_password(self, password):
        return self.password == password
    

    def insert_user(username, name, email, phone, password, is_admin, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date):
        user = User(username=username, name=name, email=email,
                    phone=phone, password=password, is_admin=is_admin,
                    card_num_card=card_num_card, card_name_owner=card_name_owner,
                    card_cvv=card_cvv, card_month_expire_date=card_month_expire_date,
                    card_year_expire_date=card_year_expire_date)
        db.session.add(user)
        db.session.commit()
        return user
