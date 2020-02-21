from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews", methods=["GET"])
def reviews_index():
    return render_template("reviews/list.html", reviews = Review.query.all())

@app.route("/reviews/new")
@login_required
def reviews_form():
    book_id = request.args.get("book_id")

    return render_template("reviews/new.html", form = ReviewForm(book_id))

@app.route("/reviews", methods=["POST"])
@login_required
def reviews_create():
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form = form)

    newReview = Review(form.rating.data, form.reviewText.data, current_user.account_id)
    
    db.session().add(newReview)
    db.session().commit()

    return redirect(url_for("index"))