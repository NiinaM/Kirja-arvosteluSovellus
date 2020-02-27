from application import db
from application.models import Base

class Review(Base):

    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, rating, review_text, book_id, account_id):
        self.rating = rating
        self.review_text = review_text
        self.book_id = book_id
        self.account_id = account_id