from application import db
from application.models import Base, Name
from application.books.models import Book

from sqlalchemy.sql import text

read_books = db.Table('read_books', Base.metadata,
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class User(Base, Name):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    #pois????
    books = db.relationship("Book", backref='account', lazy=True)
    reviews = db.relationship("Review", backref='account', lazy=True)
    
    read_books = db.relationship("Book", secondary=read_books, lazy="subquery", backref="users")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return["ADMIN"]
        #tällä hetkellä kaikki käyttäjät voivat muokata kaikkea
        #sellainen rooli kaikille, että he voivat muokata omia tekemisiään mutteivät muiden?

    @staticmethod
    def how_many_books_have_different_users_read():
        stmt = text("SELECT Account.id, Account.name, COUNT(Read_books.book_id) FROM Account "
                    "LEFT JOIN Read_books ON Read_books.account_id = Account.id "
                    "GROUP BY Account.id")
        results = db.engine.execute(stmt)

        response = []
        for row in results:
            response.append({"id":row[0], "name":row[1], "count":row[2]})

        return response