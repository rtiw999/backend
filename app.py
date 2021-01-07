from flask import Flask, redirect, url_for, session, flash
from flask_cors import CORS
import pandas as pd
import numpy as np


app = Flask(__name__)
CORS(app)


data = pd.read_excel(r'data.xlsx')
months = data.iloc[18, 1:13]
income_1 = data.iloc[22, 1:13]
total_food_1 = data.iloc[29, 1:13]
total_utility_1 = data.iloc[33, 1:13]
total_transport_1 = data.iloc[38, 1:13]


months_2 = data.iloc[18, 14:26]
income_2 = data.iloc[22, 14:26]




@app.route("/name")
def home():
    name = data.iloc[0, 0]
    return {"name": name}


@app.route("/income/<int:year>")
def annual_income(year):
    income_splice = 1 + (12 * (year-1))
    income = data.iloc[22, income_splice:(income_splice+13)]

    return {"months": months.tolist(),
            "income": income.tolist()}


@app.route("/stocks/<int:year>")
def stock_returns(year):
    stocks_splice = 1 + (12 * (year-1))
    stocks = data.iloc[21, stocks_splice:(stocks_splice+13)]
    
    return {"months": months.tolist(),
            "income": stocks.tolist()}





# if __name__ == "__main__":
#     app.run()
