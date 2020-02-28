# Kirja-arvosteluSovellus

## Aihekuvaus

Sovellukseen voi lisätä kirjoja ja siinä voi arvostella kirjoja. Käyttäjä luo käyttäjän ja voi lisätä sekä poistaa itse lisäämiään kirjoja. Kirjaa ei voi kuitenkaan poistaa, jos siinä on arvosteluja. Käyttäjä voi selata kaikkia sovelluksessa olevia kirjoja riippumatta siitä onko itse niitä lisännyt ja voi myös arvostella itse lisäämiään ja muiden lisäämiä kirjoja. Käyttäjä voi muokata itse lisäämiäänsä arvosteluja. Kirjoista näkee listan kirjojen listaussivulla ja siitä voi valita haluamansa kirjan. Kirjan omalta sivulta kirjan voi arvostella sekä merkitä itselleen luetuksi. Etusivulla on listaus. josta näkee kuinka monta kirjaa kukin käyttäjä on lukenut.

## Kirjautuminen:
Sovelluksessa on vain yhdenlaisia käyttäjiä ja yksi valmiiksi luotu tunnus, jota voi käyttää on:
* käyttäjä : Käyttäjä1
* salasana : Salasana1

![Tietokantakaavio](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/Lopullinen%20tietokantakaavio.jpg)


## Linkkejä

[Käyttötapauksia](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/userstory.md)

[Dokumentaatio](https://github.com/NiinaM/Kirja-arvosteluSovellus/tree/master/documentation)

[Heroku](https://kirjaarvostelusovellus.herokuapp.com/)


## Asennusohje

1. Lataa repositorio tai kloonaa se
2. Asenna tarvittavat riippuvuudet: 
    ```pip install requirements.txt```
3. Aja ohjelma komennolla: ```python run.py```

## Käyttöohje

* Sovelluksessa voi luoda käyttäjän painamalla "Luo uusi tunnus"-linkkiä ja kirjautua voi painamalla "Kirjaudu"-linkkiä. Ulos voi kirjautua painamalla uloskirjautumislinkkiä.
* Sovelluksessa olevat kirjat näkee "Listaa kirjat"- linkin kautta ja sovellukseen voi luoda uuden kirjan "Lisää kirja"- linkin kautta. 
