from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.books.models import Book
from application.books.forms import BookForm
from application.books.forms import BookUpdateForm

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/", methods=["GET"])
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
        return redirect(url_for("books_index"))
    
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

@app.route("/books/update/<book_id>", methods=["GET"])
@login_required
def updating_book_view(book_id):
    book = Book.query.get(book_id)
    form = BookUpdateForm()
    
    form.updated_name.data = book.name

    return render_template("books/update.html", book_id = book_id, form = form)

#Kirjan muokkaustoiminnallisuus. Kesken!
@app.route("/books/update/<book_id>", methods=["POST"])
@login_required
def book_update(book_id):
    book_for_updating = Book.query.get(book_id)
    user = current_user
    form = BookUpdateForm(request.form)
    updated_book_name = Book(form.updated_name.data)

    if not form.validate():
        return render_template("books/update.html", form = form)

    if book_for_updating.account_id != current_user.id:
        return redirect(url_for("book_view", book_id = book_id))

    book_for_updating.name = updated_book_name.name
    db.session.commit()
    return redirect(url_for("book_view", book_id = book_id))

    
