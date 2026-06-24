// Garante que o script só vai correr quando toda a página estiver carregada
document.addEventListener('DOMContentLoaded', function() {
    
    // Procura o formulário pelo ID
    const formulario = document.getElementById('formContato');
    
    // Alerta de segurança caso o formulário não seja encontrado (ajuda a detetar erros de ID)
    if (!formulario) {
        console.error("Erro crítico: O formulário com o ID 'formContato' não foi encontrado.");
        return;
    }

    // Monitoriza o momento em que o utilizador clica no botão de enviar
    formulario.addEventListener('submit', function(event) {
        
        // REGRA DE OURO: Bloqueia o envio do navegador imediatamente para forçar a validação
        event.preventDefault();

        // Captura os elementos do HTML
        const campoNome = document.getElementById('nome');
        const campoEmail = document.getElementById('email');
        const campoMensagem = document.getElementById('mensagem');

        // Verifica se houve algum erro de digitação nos IDs do HTML
        if (!campoNome || !campoEmail || !campoMensagem) {
            alert("Erro técnico: Verifique se os IDs 'nome', 'email' e 'mensagem' estão corretos no HTML.");
            return;
        }

        // Obtém os valores digitados e remove os espaços em branco desnecessários
        const nome = campoNome.value.trim();
        const email = campoEmail.value.trim();
        const mensagem = campoMensagem.value.trim();

        // REQUISITO 1: Verificar se ALGUM dos campos está vazio
        if (nome === "" || email === "" || mensagem === "") {
            alert("Por favor, preencha todos os campos do formulário antes de enviar.");
            return; // Para a execução aqui e não deixa avançar
        }

        // REQUISITO 2: Validar o formato do e-mail com Expressão Regular (Regex)
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Por favor, insira um e-mail válido (exemplo: nome@dominio.com).");
            return; // Para a execução aqui se o e-mail estiver errado
        }

        // REQUISITO 3: Se o código chegou até aqui, significa que passou em todos os testes
        alert("Mensagem enviada com sucesso!");
        
        // Limpa os campos do formulário após o sucesso
        formulario.reset();
    });
});