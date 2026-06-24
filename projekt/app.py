from flask import Flask
from models import ksiazka
from controllers.kontroler import kontroler

app = Flask(__name__)
app.register_blueprint(kontroler)

ksiazka.inicjalizuj()

if __name__ == "__main__":
    app.run(debug=True)
