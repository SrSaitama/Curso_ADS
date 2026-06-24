// Aguarda o HTML carregar completamente
document.addEventListener('DOMContentLoaded', function() {
    // Captura o botão de alternar tema
    const btnTema = document.getElementById('btn-tema');

    // PASSO 1: Verifica se o usuário já tinha escolhido o tema escuro antes
    // O localStorage guarda essa informação mesmo se fechar o navegador
    if (localStorage.getItem('tema-escolhido') === 'dark') {
        document.body.classList.add('dark-theme'); // Ativa o modo escuro
    }

    // PASSO 2: Escuta o clique no botão de alternar
    if (btnTema) {
        btnTema.addEventListener('click', function() {
            // O 'toggle' adiciona a classe se ela não existir, e remove se já existir
            document.body.classList.toggle('dark-theme');

            // PASSO 3: Salva a nova preferência na memória do navegador
            if (document.body.classList.contains('dark-theme')) {
                localStorage.setItem('tema-escolhido', 'dark'); // Salva que quer escuro
            } else {
                localStorage.setItem('tema-escolhido', 'light'); // Salva que quer claro
            }
        });
    }
});