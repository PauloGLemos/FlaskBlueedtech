from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=('GET','POST'))
def index():
    nome = None
    sobrenome = None
    criatura = None
    imagem = None

    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        criatura = request.form["criatura"]

        if criatura == "elfo":
            imagem = "https://i1.wp.com/www.valinor.com.br/wp-content/uploads/2005/06/legolas.jpg?fit=1000%2C671&ssl=1"
        elif criatura == "orc":
            imagem = "https://img.r7.com/images/orc-tatuagem-brasil-dentes-04112020111431902?dimensions=634x630"
        elif criatura == "hobbit":
            imagem = "https://www.newzealand.com/assets/Tourism-NZ/Other/85ea735179/img-1536919848-7115-17173-00A3B4F5-E6E9-CEEE-54708BDD4ECA7C3B__aWxvdmVrZWxseQo_FocalPointCropWzQyNyw2NDAsNTAsNTAsODUsImpwZyIsNjUsMi41XQ.jpg"
        else:
            imagem = None

    return render_template("index.html", nome=nome, sobrenome=sobrenome, criatura=criatura, imagem=imagem)

if(__name__ == "__main__"):
    app.run(debug=True)