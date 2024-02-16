from . import db

class Megabytes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_income = db.Column(db.String(300), unique=True)
    highest_spend = db.Column(db.String(300), unique=True)
    best_selling_item = db.Column(db.String(300), unique=True)
    worst_selling_item = db.Column(db.String(300), unique=True)
    avg_basket_spend = db.Column(db.String(300), unique=True)
    staff_mvp = db.Column(db.String(300), unique=True)
