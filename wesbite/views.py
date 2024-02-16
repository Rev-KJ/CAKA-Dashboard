from flask import Blueprint, redirect, render_template, url_for, request
from .models import Megabytes
from . import db
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("Agg")

my_view = Blueprint("my_view", __name__)

id_to_day = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

@my_view.route('/')
def home():
    week_data = Megabytes.query.all()
    if week_data:
        day_income = []
        week_day = []
        for day in week_data:
            day_income.append(day.total_income)
            week_day.append(id_to_day.get(day.id))
        print(day.total_income, day_income)
        plt.scatter(week_day, day_income)
        plt.savefig("Dashboarding/static/images/week_income.png")
    return render_template("Beta-Dash.html", week_data=week_data)

@my_view.route('/submit', methods=['POST'])
def submit():
    total_income = request.form.get('total_income')
    highest_spend = request.form.get('highest_spend')
    best_selling_item = request.form.get('best_selling_item')
    worst_selling_item = request.form.get('worst_selling_item')
    avg_basket_spend = request.form.get('avg_basket_spend')
    staff_mvp = request.form.get('staff_mvp')
    new_record = Megabytes(total_income=total_income, highest_spend=highest_spend, best_selling_item=best_selling_item, worst_selling_item=worst_selling_item, avg_basket_spend=avg_basket_spend, staff_mvp=staff_mvp)
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/edit/<data_id>", methods=["POST"])
def edit(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()

    edit_total_income = request.form.get("edit_total_income")
    edit_highest_spend = request.form.get('edit_highest_spend')
    edit_best_selling_item = request.form.get('edit_best_selling_item')
    edit_worst_selling_item = request.form.get('edit_worst_selling_item')
    edit_avg_basket_spend = request.form.get('edit_avg_basket_spend')
    edit_staff_mvp = request.form.get('edit_staff_mvp')

    data.total_income = edit_total_income
    data.highest_spend = edit_highest_spend
    data.best_selling_item = edit_best_selling_item
    data.worst_selling_item = edit_worst_selling_item
    data.avg_basket_spend = edit_avg_basket_spend
    data.staff_mvp = edit_staff_mvp

    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))