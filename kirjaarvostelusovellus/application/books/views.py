from application import app, db
from flask import render_template, request
from application.books.models import Book

@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/", methods=["POST"]) #tehty POST-pyyntö lisää uuden tehtävän pyynnössä lähetetyn lomakkeen perusteella
def books_create():
    t = Book(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
    return "hello world!"