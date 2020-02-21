from application import db
from application.models import Base
#Jossain kohtaa tätä luokkaa review on ongelma, mutta en ole varma missä
#Kun yrittää luoda uuden arvostelun sovellus hajoaa
class Review(Base):

    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String(144), nullable=False) #tekstin pituus voisi olla suurempikin

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, rating, review_text, book_id, account_id):
        self.rating = rating
        self.review_text = review_text
        self.book_id = book_id
        self.account_id = account_id
        #selvitä miten tietty kirja yhdistetään arvosteluun, niin että saa oikean kirjan.