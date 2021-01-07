from flask import Flask, render_template, redirect, url_for, session, flash
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    app.run()
