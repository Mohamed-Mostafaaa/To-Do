from flask import Blueprint, render_template

"""
This file is used to add all views pages like home, chart ...etc
"""

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("home.html")