from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("pages/home.jinja")

@app.errorhandler(404)
def notFound():
    return render_template("pages/404.jinja")
