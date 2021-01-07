from flask import Flask, render_template, redirect, url_for, session, flash


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)