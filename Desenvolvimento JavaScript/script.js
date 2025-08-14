let paragrafo = document.querySelector("#para1");

paragrafo.addEventListener("click", trocaTexto);
paragrafo.addEventListener("mouseover", mudarVerde);
paragrafo.addEventListener("mouseout", mudarVermelho)



function trocaTexto(){
    paragrafo.innerHTML = "ttt"
}


function mudarVerde(){
    paragrafo.style.background="green";

}

function mudarVermelho(){
    paragrafo.style.background="red";
}






























/*let pessoa = { nome:"Mario",
               idade: 30};

console.log(pessoa);
console.log(pessoa.nome);



let listaDesejos = ["Carro",5,"VideoGame", pessoa]; /*Array*/ 
/*
console.log(listaDesejos);
console.log(listaDesejos[1]);*/









/*const nome = "Mario";
let idade;

idade = 30;
idade = idade+1;

console.log(typeof nome);
console.log(typeof idade);

/*
if (idade>=18) {
    console.log("seja bem vindo.");
} else {
    console.log("Acesso bloqueado.");
}

/*
let mensagem1 = 'Olá ' + nome + '.';
let mensagem2 = `Sua idade é ${idade}.`;

console.log(idade)
console.log(nome);

console.log(mensagem1);
console.log(mensagem2);
*/