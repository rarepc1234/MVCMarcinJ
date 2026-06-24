from models import ksiazka

ksiazka.inicjalizuj()

przykladowe = [
    ("Pan Tadeusz", "Adam Mickiewicz", 1834),
    ("Lalka", "Bolesław Prus", 1890),
    ("Ferdydurke", "Witold Gombrowicz", 1937),
    ("Solaris", "Stanisław Lem", 1961),
    ("Wiedźmin: Ostatnie życzenie", "Andrzej Sapkowski", 1993),
]

for tytul, autor, rok in przykladowe:
    ksiazka.dodaj(tytul, autor, rok)
