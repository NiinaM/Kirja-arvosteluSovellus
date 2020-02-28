# Kirja-arvosteluSovellus

## Aihekuvaus

Sovelluksessa voi arvostella kirjoja. Käyttäjä luo käyttäjän ja voi lisätä sekä poistaa itse lisäämiään kirjoja, mutta vain jos niissä ei ole vielä yhtään arvostelua. Käyttäjä voi selata kaikkia sovelluksessa olevia kirjoja riippumatta siitä onko itse niitä lisännyt ja voi myös arvostella itse lisäämiään ja muiden lisäämiä kirjoja. Käyttäjä voi muokata itse lisäämäänsä arvostelua. Kirjoja voi järjestää jollain tapaa. Ainakin varmaan tekijän mukaan. Kirjaan voi merkitä itselleen, että onko sen jo lukenut ja kirjoissa voisi ehkä olla sellainen määrän laskeminen, että montakokertaa niitä on luettu.

### Kirjautuminen:
* käyttäjä : Käyttäjä1
* salasana : Salasana1
* Huom: Sovelluksessa toimii myös uuden tunnuksen luominen.

![Tietokantakaavio](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/Lopullinen%20tietokantakaavio.jpg)


### Linkkejä

[Käyttötapauksia](https://github.com/NiinaM/Kirja-arvosteluSovellus/blob/master/documentation/userstory.md)

[Dokumentaatio](https://github.com/NiinaM/Kirja-arvosteluSovellus/tree/master/documentation)

[Heroku](https://kirjaarvostelusovellus.herokuapp.com/)


### Asennusohje

1. Lataa repositorio tai kloonaa se
2. Asenna tarvittavat riippuvuudet: 
    ```pip install requirements.txt```
3. Aja ohjelma komennolla: ```python run.py```

### Käyttöohje

* Sovelluksessa voi luoda käyttäjän painamalla "Luo uusi tunnus"-linkkiä ja kirjautua voi painamalla "Kirjaudu"-linkkiä. Ulos voi kirjautua painamalla uloskirjautumislinkkiä.
* Sovelluksessa olevat kirjat näkee "Listaa kirjat"- linkin kautta ja sovellukseen voi luoda uuden kirjan "Lisää kirja"- linkin kautta. 
