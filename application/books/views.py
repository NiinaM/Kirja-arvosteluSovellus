from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.books.models import Book
from application.books.forms import BookForm

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
@login_required
def books_form():
    return render_template("books/new.html", form = BookForm())
  
@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_set_read(book_id):

    t = Book.query.get(book_id)
    t.read = not t.read
    db.session().commit()
  
    return redirect(url_for("book_view", book_id = t.id))
    #voisi merkata itselleen luetuksi, muttei muille?
    #toinen nappi, josta voi merkata lukemattomaksi -> samaan nappiin.

@app.route("/books/", methods=["POST"])
@login_required
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)

    t = Book(form.name.data)
    t.read = form.read.data
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
@login_required
def book_delete(book_id):
    book = Book.query.get(book_id)
    if book.account_id != current_user.id:
        #lopullinen tekeminen päättämättä
        return login_manager.unauthorized()

    db.session.delete(book)

#jokaiselle kirjalle oma sivu
@app.route("/books/<book_id>", methods=["GET"])
def book_view(book_id):
    book = Book.query.get(book_id)
    #mitä muuta?
    print(book.reviews)
    return render_template(
        "books/book.html",
        book=book,
    )