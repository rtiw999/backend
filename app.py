from flask import Flask, redirect, url_for, session, flash
from flask_cors import CORS
import pandas as pd
import numpy as np


app = Flask(__name__)
CORS(app)


data = pd.read_excel(r'data.xlsx')
months_1 = data.iloc[18, 1:13]
income_1 = data.iloc[22, 1:13]
total_food_1 = data.iloc[29, 1:13]
total_utility_1 = data.iloc[33, 1:13]
total_transport_1 = data.iloc[38, 1:13]


months_2 = data.iloc[18, 14:26]
income_2 = data.iloc[22, 14:26]




@app.route("/")
def home():
    return ", ".join(months_1.tolist())


@app.route("/income/<int:year>")
def annual_income(year):
    months = data.iloc[18, 1:13]

    income_splice = 1 + (12 * (year-1))
    income = data.iloc[22, income_splice:(income_splice+12)]

    return {"months": months,
            "income": income}




# if __name__ == "__main__":
#     app.run()
