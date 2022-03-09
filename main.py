"""
author: roni.thomas@duretechnologies.com
date: 09-02-2022
"""

from flask import Blueprint, render_template, request, send_from_directory, redirect, url_for, Response
from flask_login import login_required, current_user
from __init__ import create_app, db

main = Blueprint('main', __name__)


#index page/login page
@main.route("/")
def login():
    return render_template("login.html")


#logout page
@main.route("/logout/")
def logout():
    return render_template("logout.html")


#This web page will be loaded on successful login
@main.route("/dashboard/")
@login_required
def dashboard():
    return render_template("dashboard.html")


##### ADD ROUTES FROM HERE #####





#### ROUTES END HERE #####

# we initialize our flask app using the __init__.py function
app = create_app()

#jinja zip for multiple iteration in html table
app.jinja_env.filters['zip'] = zip

if __name__ == '__main__':
    db.create_all(app=create_app())  # create the SQLite database
    app.run(port=8080, debug=True)  # run the flask app on debug mode
