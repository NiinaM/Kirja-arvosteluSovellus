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

    user = current_user
    book = Book.query.get(book_id)
    if book.id in map(lambda book: book.id, user.read_books):
        filtered_books = list(filter(lambda b: b.id != book.id, user.read_books))
        user.read_books = filtered_books
        print("poistettiin kirja")
    else:
        user.read_books.append(book)
        print("lisättiin kirja")

    db.session().commit()
  
    return redirect(url_for("book_view", book_id = book.id))

@app.route("/books/", methods=["POST"])
@login_required
def books_create():
    form = BookForm(request.form)
    user = current_user

    if not form.validate():
        return render_template("books/new.html", form = form)

    t = Book(form.name.data)
    t.read = form.read.data
    t.account_id = current_user.id

    if t.read:
        user.read_books.append(t)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/delete/<book_id>", methods=["POST"])
@login_required
def book_delete(book_id):
    book = Book.query.get(book_id)
    if book.account_id != current_user.id:
        #lopullinen tekeminen päättämättä
        return render_template("books_index")
    
    if len(book.reviews)==0:
    #lisää viesti siitä, että kirjaa ei voi poistaa, koska sitä on arvosteltu.
        db.session.delete(book)
        db.session.commit()

    return redirect(url_for("books_index"))

@app.route("/books/<book_id>", methods=["GET"])
@login_required
def book_view(book_id):
    book = Book.query.get(book_id)
    user = current_user
    book.read = book.id in map(lambda book: book.id, user.read_books)

    print(book.reviews)
    return render_template(
        "books/book.html",
        book=book,
    )