from application import db
from application.models import Base, Name
class Book(Base, Name):

    read = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.read = False