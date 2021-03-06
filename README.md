# Kirja-arvosteluSovellus

## Aihekuvaus

Sovellukseen voi lisätä kirjoja ja siinä voi arvostella kirjoja. Käyttäjä luo käyttäjän ja voi lisätä sekä poistaa itse lisäämiään kirjoja. Kirjaa ei voi kuitenkaan poistaa, jos siinä on arvosteluja. Käyttäjä voi selata kaikkia sovelluksessa olevia kirjoja riippumatta siitä onko itse niitä lisännyt ja voi myös arvostella itse lisäämiään ja muiden lisäämiä kirjoja. Käyttäjä voi muokata itse lisäämiäänsä arvosteluja. Kirjoista näkee listan kirjojen listaussivulla ja siitä voi valita haluamansa kirjan. Kirjan omalta sivulta kirjan voi arvostella sekä merkitä itselleen luetuksi. Etusivulla on listaus. josta näkee kuinka monta kirjaa kukin käyttäjä on lukenut.

## Kirjautuminen:
Sovelluksessa on vain yhdenlaisia käyttäjiä ja yksi valmiiksi luotu tunnus, jota voi käyttää on:
* käyttäjä : Käyttäjä1
* salasana : Salasana1

![Tietokantakaavio](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/Lopullinen%20tietokantakaavio.jpg)


## [Linkkejä dokumentaatioon](https://github.com/NiinaM/Kirja-arvosteluSovellus/tree/master/documentation)

[Asennusohje](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/installingIntroduction.md)

[Käyttöohje](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/usermanual.md)

[Käyttötapauksia](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/userstory.md)

[Heroku](https://kirjaarvostelusovellus.herokuapp.com/)

[Jatkokehitysideoita](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/furtherDevelopment.md)

## Tietokantataulut

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)
CREATE TABLE book (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
CREATE TABLE review (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	rating INTEGER NOT NULL, 
	review_text VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	book_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(book_id) REFERENCES book (id)
)
CREATE TABLE read_books (
	account_id INTEGER, 
	book_id INTEGER, 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(book_id) REFERENCES book (id)
)

```
