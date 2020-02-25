from application import db
from application.models import Base, Name
#kirjan luokka
class Book(Base, Name):

    reviews = db.relationship("Review", backref='book', lazy=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.read = False