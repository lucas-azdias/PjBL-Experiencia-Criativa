use pjbl_exp_criativa;

# USER
insert into users(username, name, email, phone, password, is_admin, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date)
values ("bafome", "Bafomé Pinto Carvalho", "bafome@gmail.com", "+5511999998888", "jesus", true, "1234123412341234", "Bafomé P Carvalho", "123", 01, 2040);

# PAYMENT
insert into payments(id_user, value, month, year, is_paid, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date)
values (1, 19.99, 05, 2023, true, "1234123412341234", "Bafomé P Carvalho", "123", 01, 2040);
