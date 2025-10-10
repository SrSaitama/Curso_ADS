let botao = document.querySelector("#botao");
let estaQuebrado = false;
botao.style.background="blue";




botao.addEventListener("mouseover",e =>{
    if(estaQuebrado==false)
    botao.style.background="green"
});

botao.addEventListener("mouseout",e =>{
    if(!estaQuebrado)
    botao.style.background="blue"
});


botao.addEventListener("click", e =>{
    botao.style.background="red";
    botao.innerHTML="quebrei"
    estaQuebrado = true;
});


/*
botao.addEventListener("mouseover", trocaVerde);

function trocaVerde(){
    botao.style.background="green";
}

*/