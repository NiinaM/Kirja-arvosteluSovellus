from application import db
from application.models import Base, Name

class Book(Base, Name):

    read = db.Column(db.Boolean, nullable=False)

    reviews = db.relationship("Review", backref='book', lazy=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.read = False