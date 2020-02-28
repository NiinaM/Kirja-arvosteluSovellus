## Käyttötapauksia

- [x] Käyttäjänä voin lisätä kirjan.
- [x] Käyttäjänä voin poistaa itse lisäämäni kirjan, jossa ei ole arvostelua.
- [x] Käyttäjänä voin arvostella, minkä hyvänsä kirjan.
- [x] Käyttäjänä voin poistaa itse tekemäni arvostelun.
- [x] Käyttäjänä voin muokata lisäämäni kirjan nimeä.
- [x] Käyttäjänä voin muokata kirjoittamani arvostelun arvosanaa.
- [x] Käyttäjänä voin muokata kirjoittamani arvostelun tekstiosaa.
- [x] Käyttäjänä voin merkitä minkä hyvänsä kirjan luetuksi.
- [x] Käyttäjänä voin merkitä minkä hyvänsä kirjan lukemattomaksi.
- [x] Kuka vain voi luoda käyttäjätunnuksen.
- [x] Kuka vain näkee etusivulla koosteen käyttäjien lukemien kirjojen määrästä.
```
"SELECT Account.id, Account.name, COUNT(Read_books.book_id) FROM Account "
"LEFT JOIN Read_books ON Read_books.account_id = Account.id "
"GROUP BY Account.id"
```
- [x] Kuka vain näkee kaikkien kirjojen keskiarvollisen arvosanan.
```
"SELECT Book.id, Book.name, AVG(Review.rating) FROM Book "
"LEFT JOIN Review ON Review.book_id = Book.id "
"GROUP BY Book.id "
```
- [x] Kuka vain näkee listan kaikista sivulla olevista kirjoista.

### Tekemättä jääneet käyttötapaukset
* Käyttäjänä voin listata kirjat tekijän mukaan.
* Käyttäjänä voin selata lukemiani kirjoja.
