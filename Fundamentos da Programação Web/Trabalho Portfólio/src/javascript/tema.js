//Garante que o script só vai iniciar quando a pagina terminar de carregar
document.addEventListener('DOMContentLoaded', function(){

    const butTema = document.getElementById('btn-tema');

    //VERIFICA SE O USUARIO JÁ ESCOLHEU O TEMA ESCURO,
    //O localStorage vai guardar a decisão do usuario. 
    if(localStorage.getItem('tema-escolhido') == 'dark') {
        document.body.classList.add('dark-theme');
    }

    //Verificar se o usuario apertou o botão
    if(butTema) {
        butTema.addEventListener('click', function(){
            document.body.classList.toggle('dark-theme');

            if(document.body.classList.contains('dark-theme')){
                localStorage.setItem('tema-escolhido', 'dark');
            
            } else {
                localStorage.setItem('tema-escolhido', 'light')
            }
        });
    }

});