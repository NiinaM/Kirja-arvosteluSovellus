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
        stmt = text("SELECT Book.id, Book.name, AVG(Review.rating) FROM Book "
                    "LEFT JOIN Review ON Review.book_id = Book.id "
                    "GROUP BY Book.id ")
        results = db.engine.execute(stmt)

        response = []
        for row in results:
            id = row[0]
            name = row[1]
            avg = row[2]

            if not row[2]:
                avg = ""
            else:
                avg = '{0:.1f}'.format(row[2])
            response.append({"id":id, "name":name, "avg":avg})

        return response