from application import db
from application.models import Base, Name
from application.books.models import Book

from sqlalchemy.sql import text

#liitostaulu
read_books = db.Table('read_books', Base.metadata,
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class User(Base, Name):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    books = db.relationship("Book", backref='account', lazy=True)
    reviews = db.relationship("Review", backref='account', lazy=True)
    #yhteys liitostauluun, niin että saa "napin" toimimaan oikein. Ei toimi oikein tällä hetkellä.
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

    #yhteenvetokyselyt pitäisi saada toimimaan herokussa!!!
    #@staticmethod
    #def find_users_with_nothing_to_read(read=0):
      #  stmt = text("SELECT Account.id, Account.name FROM Account"
       #              " LEFT JOIN Book ON Book.account_id = Account.id"
        #             " WHERE (Book.read IS null OR Book.read = :read)"
         #            " GROUP BY Account.id"
          #           " HAVING COUNT(Book.id) = 0").params(read=read)
        #res = db.engine.execute(stmt)

        #response = []
        #for row in res:
         #   response.append({"id":row[0], "name":row[1]})

        #return response