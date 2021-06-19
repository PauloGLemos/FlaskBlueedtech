const pessoa = {
  nome: "Betão ",
  sobrenome: "Einstein",
  idade: 42,

  doido: true,

  imagemserio:"./imagem/01.jpg",
  imagemdoido:"./imagem/02.jpg",
}

const elementonome = document.getElementById('nome');
const elementosobrenome = document.getElementById('sobrenome');
const elementoidade = document.getElementById('idade');
const elementobotao = document.getElementById('alteraHumor');

elementonome.innerText = pessoa.nome;
elementosobrenome.innerText = pessoa.sobrenome;
elementoidade.innerText = pessoa.idade;

function alteraHumor(){
  pessoa.doido = !pessoa.doido;
  const elemenimagem = document.getElementById('imagem');
  const elementohumor = document.getElementById('blocoHumor');

  if (pessoa.doido){
    elemenimagem.src = pessoa.imagemdoido;
    elementohumor.innerHTML = pessoa.nome + ' tá <b>DOIDO !</b>';
  }
  else {
    elemenimagem.src = pessoa.imagemserio;
    elementohumor.innerHTML = pessoa.nome + 'tá <b>SÉRIO !</b>';
  }
}

alteraHumor();

elementobotao.addEventListener("click", alteraHumor);
