from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    pokemons = [
        {
            'numero': '133',
            'nome': '#133 - Eevee'
        },{
            'numero': '134',
            'nome': '#134 - Vaporeon'
        },{
            'numero': '135',
            'nome': '#135 - Jolteon'
        },{
            'numero': '136',
            'nome': '#136 - Flareon'
        },{
            'numero': '196',
            'nome': '#196 - Espeon'
        },{
            'numero': '197',
            'nome': '#197 - Umbreon'
        },{
            'numero': '470',
            'nome': '#470 - Leafon'
        },{
            'numero': '471',
            'nome': '#471 - Glaceon'
        },{
            'numero': '700',
            'nome': '#700 - Sylveon'
        },
    ]
    caminho_base='http://assets.pokemon.com/assets/cms2/img/pokedex/detail/'

    return render_template("index.html", pokemons=pokemons, caminho_base=caminho_base)

if (__name__ == "__main__"):
    app.run(debug=True)
