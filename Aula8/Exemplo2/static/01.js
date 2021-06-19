const cardPokemons = document.querySelectorAll(".card-pokemon");
const pokemonSelecionado = document.querySelector("#pokemon-selecionado");

function selecionaPokemon(){
    const nomePokemon =  this.getAttribute("data-nome");

    if(!this.classList.contains("selecionado")){
        this.classList.add("selecionado");
        pokemonSelecionado.innerHTML = `O ultimo Pokemon Selecionado foi o <b>${nomePokemon}</b>`;
        //pokemonSelecionado.innerHTML = "O ultimo Pokemon Selecionado foi o: <b>"+nomePokemon+"</b>";
    }
    else{
        this.classList.remove("selecionado");

        const pokemonsSelecionado = document.querySelectorAll(".selecionado")
        if(pokemonSelecionado.lenght >= 1 ){
            pokemonSelecionado.innerHTML = `Voce deselecionou o pokemon ${nomePokemon}. ainda falta(m) ${pokemonsSelecionado.length} selecionado(s).`
        }
        else{
            pokemonSelecionado.innerHTML = "Selecione um Pokemon"
        }
    }

}

for(const cardPokemon of cardPokemons){
    cardPokemon.addEventListener("click", selecionaPokemon)
}