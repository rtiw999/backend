from flask import Flask, render_template, redirect, url_for, session, flash
from flask_cors import CORS
import pandas as pd
import numpy as np


app = Flask(__name__)
CORS(app)


data = pd.read_excel(r'data.xlsx')
months_1 = data.iloc[18, 1:13]
income_1 = data.iloc[22, 1:13]

months_2 = data.iloc[18, 14:26]




@app.route("/")
def home():
    return ", ".join(months_1.tolist())


# if __name__ == "__main__":
#     app.run()
