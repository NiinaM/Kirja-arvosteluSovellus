## Käyttötapauksia


### SQLalchemyn generoimat tietokantakyselyt
- [x] Kuka vain voi luoda käyttäjätunnuksen.
```
INSERT INTO account (date_created, date_modified, name, username, password) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)

```
- [x] Käyttäjä voi kirjautua sisään.
```
SELECT account.id AS account_id, account.date_created AS account_date_created, 
account.date_modified AS account_date_modified, account.name AS account_name, 
account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.password = ? AND account.username = ?
LIMIT ? OFFSET ?

```
- [x] Käyttäjä voi kirjautua ulos.
```
SELECT account.id AS account_id, account.date_created AS account_date_created, 
account.date_modified AS account_date_modified, account.name AS account_name, 
account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.id = ?

```
- [x] Käyttäjänä voin lisätä kirjan.
```
INSERT INTO book (date_created, date_modified, name, account_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```
- [x] Käyttäjänä voin poistaa itse lisäämäni kirjan, jossa ei ole arvostelua.
```
DELETE FROM book WHERE book.id = ?
```
- [x] Käyttäjänä voin arvostella, minkä hyvänsä kirjan.
```
INSERT INTO review (date_created, date_modified, rating, review_text, 
account_id, book_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```
- [x] Käyttäjänä voin poistaa itse tekemäni arvostelun.
```
DELETE FROM review WHERE review.id = ?

```
- [x] Käyttäjänä voin muokata lisäämäni kirjan tietoja.
```
UPDATE book SET date_modified=CURRENT_TIMESTAMP, name=? WHERE book.id = ?

```
- [x] Käyttäjänä voin muokata kirjoittamani arvostelua.
```
UPDATE review SET date_modified=CURRENT_TIMESTAMP, rating=? WHERE review.id = ?
```
- [x] Käyttäjänä voin merkitä minkä hyvänsä kirjan luetuksi.
```
INSERT INTO read_books (account_id, book_id) VALUES (?, ?)
```
- [x] Käyttäjänä voin merkitä minkä hyvänsä kirjan lukemattomaksi.
```
DELETE FROM read_books WHERE read_books.account_id = ? AND read_books.book_id = ?
```
### Itsetehdyt tietokantakyselyt
- [x] Kuka vain näkee etusivulla koosteen käyttäjien lukemien kirjojen määrästä.
```
"SELECT Account.id, Account.name, COUNT(Read_books.book_id) FROM Account "
"LEFT JOIN Read_books ON Read_books.account_id = Account.id "
"GROUP BY Account.id"
```
- [x] Kuka vain näkee kaikkien kirjojen nimen ja keskiarvollisen arvosanan.
```
"SELECT Book.id, Book.name, AVG(Review.rating) FROM Book "
"LEFT JOIN Review ON Review.book_id = Book.id "
"GROUP BY Book.id "
```
### Tekemättä jääneet käyttötapaukset
* Käyttäjänä voin listata kirjat tekijän mukaan.
* Käyttäjänä voin selata lukemiani kirjoja.
