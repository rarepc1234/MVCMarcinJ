# Cyfrowa Biblioteka

## Spis treści

- [Opis projektu](#opis-projektu)
- [Funkcjonalności](#funkcjonalności)
- [Struktura projektu](#struktura-projektu)
- [Instrukcja obsługi](#instrukcja-obsługi)

## Opis projektu

Aplikacja internetowa do zarządzania cyfrową biblioteką, zbudowana w technologii Python Flask z wykorzystaniem wzorca architektonicznego MVC. Umożliwia przeglądanie, dodawanie, edycję oraz usuwanie książek.

## Funkcjonalności

- Wyświetlanie listy wszystkich książek
- Dodawanie nowej książki
- Edycja istniejącej książki
- Usuwanie książki

Każda książka opisana jest przez tytuł, autora oraz rok wydania.

## Struktura projektu

Projekt zrealizowany zgodnie ze wzorcem MVC:

- `models/ksiazka.py` — Model: definicja danych książki oraz operacje na bazie danych
- `controllers/kontroler.py` — Kontroler: obsługa żądań HTTP, interakcja z modelem, przekazywanie danych do widoku
- `templates/` — Widok: lista widoków oraz formularz dodawania i edycji
- `static/style.css` — arkusz stylów
- `app.py` — uruchomienie aplikacji
- `dane_przykladowe.py` — załadowanie przykładowych danych wejściowych

## Instrukcja obsługi

1. Zainstaluj wymagane paczki:

```
pip install -r requirements.txt
```

2. Załaduj przykładowe dane wejściowe:

```
python dane_przykladowe.py
```

3. Uruchom aplikację:

```
python app.py
```

4. Otwórz w przeglądarce adres:

```
http://127.0.0.1:5000
```
