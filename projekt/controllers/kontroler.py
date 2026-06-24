from flask import Blueprint, render_template, request, redirect, url_for
from models import ksiazka

kontroler = Blueprint("kontroler", __name__)


@kontroler.route("/")
def lista():
    ksiazki = ksiazka.pobierz_wszystkie()
    return render_template("lista.html", ksiazki=ksiazki)


@kontroler.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        tytul = request.form["tytul"]
        autor = request.form["autor"]
        rok_wydania = request.form["rok_wydania"]
        ksiazka.dodaj(tytul, autor, rok_wydania)
        return redirect(url_for("kontroler.lista"))
    return render_template("formularz.html", ksiazka=None)


@kontroler.route("/edytuj/<int:ksiazka_id>", methods=["GET", "POST"])
def edytuj(ksiazka_id):
    pozycja = ksiazka.pobierz_po_id(ksiazka_id)
    if request.method == "POST":
        tytul = request.form["tytul"]
        autor = request.form["autor"]
        rok_wydania = request.form["rok_wydania"]
        ksiazka.aktualizuj(ksiazka_id, tytul, autor, rok_wydania)
        return redirect(url_for("kontroler.lista"))
    return render_template("formularz.html", ksiazka=pozycja)


@kontroler.route("/usun/<int:ksiazka_id>")
def usun(ksiazka_id):
    ksiazka.usun(ksiazka_id)
    return redirect(url_for("kontroler.lista"))
