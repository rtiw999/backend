from flask import Flask, redirect, url_for, session, flash
from flask_cors import CORS
import pandas as pd
import numpy as np


app = Flask(__name__)
CORS(app)


data = pd.read_excel(r'data.xlsx')
months = data.iloc[18, 1:13]


def splice(x: int):
    return 1 + (13 * (x-1))



@app.route("/name")                     # returns the name of the user
def home():
    name = data.iloc[0, 0]
    return {"data": "name",
            "name": name}


@app.route("/income/<int:year>")        # gets the job income, drop shipping income, stock return, and total income
def annual_income(year):
    income_splice = splice(year)
    income = data.iloc[22, income_splice:(income_splice+12)]
    job = data.iloc[19, income_splice:(income_splice+12)]
    drop = data.iloc[20, income_splice:(income_splice+12)]
    stocks = data.iloc[21, income_splice:(income_splice + 12)]

    return {"data": "months, job, drop, stocks, total_income",
            "months": months.tolist(),
            "job": job.tolist(),
            "drop": drop.tolist(),
            "stocks": stocks.tolist(),
            "total_income": income.tolist()}


@app.route("/utility/<int:year")
def utility_costs(year):
    utility_splice = splice(year)
    water = data.iloc[31, utility_splice:(utility_splice+12)]
    power = data.iloc[32, utility_splice:(utility_splice+12)]
    total_utility = data.iloc[33, utility_splice:(utility_splice+12)]

    return {"data": "months, water, power, total_utility",
            "months": months.tolist(),
            "water": water.tolist(),
            "power": power.tolist(),
            "total_utility": total_utility.tolist()}


@app.route("/food/<int:year>")
def food_costs(year):
    food_splice = splice(year)
    groceries = data.iloc[27, food_splice:(food_splice+12)]
    eating_out = data.iloc[28, food_splice:(food_splice+12)]
    total_food = data.iloc[29, food_splice:(food_splice+12)]

    return {"data": "months, groceries, eating_out, total_food",
            "months": months.tolist(),
            "groceries": groceries.tolist(),
            "eating_out": eating_out.tolist(),
            "total_food": total_food.tolist()}


@app.route("/transportation/<int:year>")
def transport(year):
    transport_splice = splice(year)
    public = data.iloc[35, transport_splice:(transport_splice+12)]
    flights = data.iloc[36, transport_splice:(transport_splice+12)]
    rideshare = data.iloc[37, transport_splice:(transport_splice+12)]
    total_transportation = data.iloc[38, transport_splice:(transport_splice+12)]

    return {"data": "months, public, flights, rideshare, transportation",
            "months": months.tolist(),
            "public": public.tolist(),
            "flights": flights.tolist(),
            "rideshare": rideshare.tolist(),
            "total_transportation": total_transportation.tolist()}


@app.route("/subscriptions/<int:year>")
def sub(year):
    subscribe_splice = splice(year)
    subscribe = data.iloc[43, subscribe_splice:(subscribe_splice+12)]

    return {"data": "months, subscriptions",
            "months": months.tolist(),
            "subscriptions": subscribe.tolist()}


@app.route("/other/<int:year>")
def others(year):
    other_splice = splice(year)
    other_expenses = data.iloc[45, other_splice:(other_splice+12)]

    return {"data": "other",
            "months": months.tolist(),
            "other": other_expenses.tolist()}


@app.route("/total/<int:year>")
def total_expenses(year):
    total_splice = splice(year)
    total = data.iloc[47, total_splice:(total_splice+12)]

    return {"data": "total",
            "months": months.tolist(),
            "total": total.tolist()}




@app.route("/subscription_list")
def subs():
    things = data.iloc[40:43, 0]

    return {"data": "subscription services",
            "services": things.tolist()}





# if __name__ == "__main__":
#     app.run()
