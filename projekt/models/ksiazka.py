import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "biblioteka.db")


def polacz():
    polaczenie = sqlite3.connect(DB_PATH)
    polaczenie.row_factory = sqlite3.Row
    return polaczenie


def inicjalizuj():
    polaczenie = polacz()
    polaczenie.execute(
        """
        CREATE TABLE IF NOT EXISTS ksiazki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tytul TEXT NOT NULL,
            autor TEXT NOT NULL,
            rok_wydania INTEGER NOT NULL
        )
        """
    )
    polaczenie.commit()
    polaczenie.close()


def pobierz_wszystkie():
    polaczenie = polacz()
    wiersze = polaczenie.execute("SELECT * FROM ksiazki ORDER BY id").fetchall()
    polaczenie.close()
    return wiersze


def pobierz_po_id(ksiazka_id):
    polaczenie = polacz()
    wiersz = polaczenie.execute(
        "SELECT * FROM ksiazki WHERE id = ?", (ksiazka_id,)
    ).fetchone()
    polaczenie.close()
    return wiersz


def dodaj(tytul, autor, rok_wydania):
    polaczenie = polacz()
    polaczenie.execute(
        "INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)",
        (tytul, autor, rok_wydania),
    )
    polaczenie.commit()
    polaczenie.close()


def aktualizuj(ksiazka_id, tytul, autor, rok_wydania):
    polaczenie = polacz()
    polaczenie.execute(
        "UPDATE ksiazki SET tytul = ?, autor = ?, rok_wydania = ? WHERE id = ?",
        (tytul, autor, rok_wydania, ksiazka_id),
    )
    polaczenie.commit()
    polaczenie.close()


def usun(ksiazka_id):
    polaczenie = polacz()
    polaczenie.execute("DELETE FROM ksiazki WHERE id = ?", (ksiazka_id,))
    polaczenie.commit()
    polaczenie.close()
