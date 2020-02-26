from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews/new")
@login_required
def reviews_form():
    book_id = request.args.get("book_id")
    form = ReviewForm()
    form.book_id.data = book_id

    return render_template("reviews/new.html", form = form)

@app.route("/reviews", methods=["POST"])
@login_required
def reviews_create():
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form = form)

    newReview = Review(form.rating.data, form.reviewText.data, form.book_id.data, current_user.id)
    
    db.session().add(newReview)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/reviews/delete/<review_id>", methods=["POST"])
@login_required
def review_delete(review_id):
    review = Review.query.get(review_id)
    book_id = review.book_id
    if review.account_id != current_user.id:
        #Ehkä jokin viesti siitä, ettei arvostelua voi poistaa, koska joku muu on sen kirjoittanut tai edes paluu samaa näkymää 
        return redirect(url_for("book_view", book_id = book_id))
    
    db.session.delete(review)
    db.session.commit()

    return redirect(url_for("book_view", book_id = book_id))