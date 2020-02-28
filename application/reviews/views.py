from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews/new", methods=["GET"])
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

    return redirect(url_for("book_view", book_id = form.book_id.data))

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

@app.route("/reviews/update/<review_id>", methods=["GET"])
@login_required
def updating_review_view(review_id):
    review = Review.query.get(review_id)
    form = ReviewForm(request.form)

    form.rating.data = review.rating
    form.reviewText.data = review.review_text

    return render_template("reviews/update.html", review_id = review_id, form = form)

@app.route("/reviews/update/<review_id>", methods=["POST"])
@login_required
def review_update(review_id):
    review_for_updating = Review.query.get(review_id)
    user = current_user
    book_id = review_for_updating.book_id
    form = ReviewForm(request.form)

    updated_review_rating = form.rating.data
    updated_review_text = form.reviewText.data
    
    if not form.validate():
        return render_template("reviews/update.html", form = form)

    if review_for_updating.account_id != user.id:
        return redirect(url_for("updating_review_view", review_id = review_id))

    review_for_updating.rating = updated_review_rating
    review_for_updating.review_text = updated_review_text

    db.session.commit()
    return redirect(url_for("book_view", book_id = book_id))
