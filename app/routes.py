from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from .charts import (
    create_expenses_chart, create_category_chart,
    create_yearly_expenses_chart, create_daily_total_chart,
    create_monthly_investment_chart, create_yearly_investment_chart
)
from .data_handler import refresh_sheet_data

main = Blueprint('main', __name__)

@main.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user.id)

@main.route("/plot")
@login_required
def plot():
    return render_template("plots.html",
                           expenses_chart=create_expenses_chart(),
                           category_chart=create_category_chart(),
                           yearly_chart=create_yearly_expenses_chart(),
                           daily_chart=create_daily_total_chart())

@main.route("/investments")
@login_required
def investments():
    return render_template("investments.html",
                           monthly_chart=create_monthly_investment_chart(),
                           yearly_chart=create_yearly_investment_chart())

@main.route("/refresh_data")
@login_required
def refresh_data():
    refresh_sheet_data()
    return jsonify({"status": "success", "message": "Data refreshed successfully"})