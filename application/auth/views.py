from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import SignInForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)


    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Ei ole olemassa tällaista käyttäjää tai salasanaa.")


    login_user(user)
    #kokeiluprintti
    print(user.read_books)
    return redirect(url_for("index")) 

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

#Salasanan järkevä luominen puuttuu vielä!
@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = SignInForm())

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = SignInForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    new_user = User(form.name.data, form.username.data, form.password.data)
 
    db.session().add(new_user)
    db.session().commit()

    user = User.query.filter_by(username=new_user.username).first()
    login_user(user)

    return redirect(url_for("index"))
