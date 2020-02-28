from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", how_many_books=User.how_many_books_have_different_users_read())