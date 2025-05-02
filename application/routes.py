from application import app , db
from flask import flash, redirect, render_template, url_for
from application.form import UserInputForm
from application.models import IncomeExpenses
import json

@app.route("/")
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template('index.html',title='index',entries=entries)

@app.route("/add", methods=["GET","POST"])
def layout():
    form = UserInputForm()
    if form.is_valid_on_submit():
        entry = IncomeExpenses(type=form.type.data, amount=form.amount.data, category=form.category.data)
        db.session.add(entry)
        db.session.commit()
        flash("Successful entry", 'Sucess')
        return redirect(url_for('index'))
    return render_template("add.html",title='add',form=form)


@app.route('/delete/<int:entry_id>')
def delete(entry_id):

    entry = IncomeExpenses.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Deletion was success", 'success')
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    income_vs_expenses = db.session.query(db.func.sum(IncomeExpenses.amount),IncomeExpenses.type).group_by(IncomeExpenses.type).order_by(IncomeExpenses.type).all()

    dates = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.date).group_by(IncomeExpenses.date).order_by(IncomeExpenses.date).all()

    income_expense = []

    for total_amount, _ in income_vs_expenses:
        income_expense.append(total_amount)

    over_time_expenditure = []
    dates_labels = []

    for amount,date in dates:
        over_time_expenditure.append(amount)
        dates_labels.append(date.strftime("%m-%d-%y"))

    return render_template("dashboard.html",income_vs_expenses = json.dumps(income_expense))