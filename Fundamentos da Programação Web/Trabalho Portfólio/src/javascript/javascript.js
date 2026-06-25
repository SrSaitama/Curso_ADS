//Garante que o script só roda depois que a pagina carregar
document.addEventListener('DOMContentLoaded', function(){
    
    //Procura o ID do formulario
    const formulario = document.getElementById('formContato');

   
    //Verificar se o botão de enviar foi apertado
    formulario.addEventListener('submit', function(event){

        //Bloquear envio, para validar os dados antes.
        event.preventDefault();

        //Captura os elementos
        const campoNome = document.getElementById('nome');
        const campoEmail = document.getElementById('email');
        const campoMensagem = document.getElementById('mensagem');

  

        //Recebe os valores digitados
        const nome = campoNome.value.trim();
        const email = campoEmail.value.trim();
        const mensagem = campoMensagem.value.trim();

    
        //Verifica se tem campos vazios
        if(nome === "" || email === "" || mensagem === ""){
            alert("Por favor, preencha todos os campos!")
            return;
        }

        //Validar o formato do email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Por favor, insira um e-mail válido (exemplo: nome@dominio.com).");
            return;
        }

        //Confirma que a mensagem foi enviada
        alert("Mensagem enviada!");

        //Limpa o formulario apos o envio
        formulario.reset();
    
    });
});