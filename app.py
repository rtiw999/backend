from flask import Flask, redirect, url_for, session, flash, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime
import operator


app = Flask(__name__)
CORS(app)


data = pd.read_excel(r'data.xlsx')

current_month = 12                      # month is December
current_year = 2                        # year is 2020

end = 1 + (12 * (current_year-1)) + current_month

def splice(x: int):
    return 1 + (13 * (x-1))



@app.route("/name")                     # returns the name of the user
def home():
    name = data.iloc[0, 0]
    return {"data": "name",
            "name": name}


@app.route("/income/<int:months_back>")        # gets the job income, drop shipping income, stock return, and total income
def annual_income(months_back):
    months = data.iloc[18, end-months_back:end]
    income = data.iloc[22, end-months_back:end]
    job = data.iloc[19, end-months_back:end]
    drop = data.iloc[20, end-months_back:end]
    stocks = data.iloc[21, end-months_back:end]

    return {"data": "months, job, drop, stocks, total_income",
            "months": months.tolist(),
            "job": job.tolist(),
            "drop": drop.tolist(),
            "stocks": stocks.tolist(),
            "total_income": income.tolist()}


@app.route("/utility/<int:months_back>")
def utility_costs(months_back):
    months = data.iloc[18, end-months_back:end]
    water = data.iloc[31, end-months_back:end]
    power = data.iloc[32, end-months_back:end]
    total_utility = data.iloc[33, end-months_back:end]

    return {"data": "months, water, power, total_utility",
            "months": months.tolist(),
            "water": water.tolist(),
            "power": power.tolist(),
            "total_utility": total_utility.tolist()}


@app.route("/food/<int:months_back>")
def food_costs(months_back):
    months = data.iloc[18, end-months_back:end]
    groceries = data.iloc[27, end-months_back:end]
    eating_out = data.iloc[28, end-months_back:end]
    total_food = data.iloc[29, end-months_back:end]

    return {"data": "months, groceries, eating_out, total_food",
            "months": months.tolist(),
            "groceries": groceries.tolist(),
            "eating_out": eating_out.tolist(),
            "total_food": total_food.tolist()}


@app.route("/transportation/<int:months_back>")
def transport(months_back):
    months = data.iloc[18, end-months_back:end]
    public = data.iloc[35, end-months_back:end]
    flights = data.iloc[36, end-months_back:end]
    rideshare = data.iloc[37, end-months_back:end]
    total_transportation = data.iloc[38, end-months_back:end]

    return {"data": "months, public, flights, rideshare, transportation",
            "months": months.tolist(),
            "public": public.tolist(),
            "flights": flights.tolist(),
            "rideshare": rideshare.tolist(),
            "total_transportation": total_transportation.tolist()}


@app.route("/subscriptions/<int:months_back>")
def sub(months_back):
    months = data.iloc[18, end-months_back:end]
    subscribe = data.iloc[43, end-months_back:end]

    return {"data": "months, subscriptions",
            "months": months.tolist(),
            "subscriptions": subscribe.tolist()}


@app.route("/other/<int:months_back>")
def others(months_back):
    months = data.iloc[18, end-months_back:end]
    other_expenses = data.iloc[45, end-months_back:end]

    return {"data": "months, other",
            "months": months.tolist(),
            "other": other_expenses.tolist()}


@app.route("/total/<int:months_back>")
def total_expenses(months_back):
    months = data.iloc[18, end-months_back:end]
    total = data.iloc[47, end-months_back:end]

    return {"data": "months, total",
            "months": months.tolist(),
            "total": total.tolist()}


@app.route("/difference/<int:months_back>")
def budget_expenses(months_back):
    months = data.iloc[18, end-months_back:end].tolist()
    income = data.iloc[22, end-months_back:end].tolist()
    expenses = data.iloc[47, end-months_back:end].tolist()

    difference_list = list(map(operator.sub, income, expenses))
    num_list = [i for i in range(months_back)]

    my_date = datetime.now()
    months.append(my_date.strftime("%B"))

    difference_np = np.array(difference_list)
    num_np = np.array(num_list)

    m, b = np.polyfit(num_np, difference_np, 1)


    difference_list.append(m*(num_list[-1]+1) + b)

    return {"data": "months, total",
            "months": months,
            "difference": difference_list}




@app.route("/subscription_list")
def subs():
    things = data.iloc[40:43, 0]

    return {"data": "services",
            "services": things.tolist()}


@app.route("/")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"{name}\n{age}\n{datetime.now().month}\n{datetime.now().year}\n{end}"


