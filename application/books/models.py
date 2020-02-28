from application import db
from application.models import Base, Name

from sqlalchemy.sql import text

class Book(Base, Name):

    reviews = db.relationship("Review", backref='book', lazy=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.read = False

    
    @staticmethod
    def average_rating_of_book():
        stmt = text("SELECT Book.id, Book.name, Review.rating FROM Book "
                    "LEFT JOIN Review ON Review.book_id = Book.id "
                    "GROUP BY Book.id "
                    "AVG()")
        results = db.engine.execute(stmt)

        response = []
        for row in results:
            print(row)
            response.append({"id":row[0], "name":row[1], "avg":row[2]})

        return response