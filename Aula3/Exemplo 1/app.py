from os import name
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"<h1>Hello, Flask! Aula3 teste1<h1>"

@app.route("/route2/<nome>")
def rota2(nome=None):
    return"<h3>Hello "+nome+" Flask!<h3>"

if (__name__ == "__main__"):
    app.run(debug=True)

    