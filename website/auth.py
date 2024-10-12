from flask import Blueprint, render_template

"""
This file is used to add all pages that need authentication like: Login, SignUp, Logout
"""

auth = Blueprint('auth', __name__)

@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "logout"