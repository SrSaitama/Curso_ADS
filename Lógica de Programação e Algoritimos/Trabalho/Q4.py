print("Bem vindo a Lista de Contatos do Bruno Eliakim")
# Variável de controle do ID Global
id_global = 5558147
# Lista para armazenar contatos (cada contato será um dicionário dentro da lista)
lista_contatos = []

# Função responsável por desenhar os traços dos menus.
def desenhar_linhas(n):
    lines = "-" * n
    return lines

# Função responsável pelas mensagens dos menus.
mensagem = {
    "Principal": [
        desenhar_linhas(50),
        f"{desenhar_linhas(15)} MENU PRINCIPAL {desenhar_linhas(15)}",
        "1 - Cadastrar Contato",
        "2 - Consultar Contato",
        "3 - Remover Contato",
        "4 - Sair",
    ],
    "Registrar": [
        desenhar_linhas(50),
        f"{desenhar_linhas(15)} MENU CADASTRAR CONTATO {desenhar_linhas(15)}",
    ],
    "Consultar":[
        desenhar_linhas(50),
        f"{desenhar_linhas(15)} MENU CONSULTAR CONTATOS {desenhar_linhas(15)}",
            "Qual opção deseja:",
            "1 - Consultar Todos",
            "2 - Consultar por Id",
            "3 - Consultar por Setor",
            "4 - Retomar ao menu",
    ],
    "Remover":[
        desenhar_linhas(50),
        f"{desenhar_linhas(15)} MENU REMOVER CONTATO {desenhar_linhas(15)}",
    ],
}

# Função que mostra várias mensagens passadas como argumento (usada para exibir menus)
def mostrar_mensagens(*args):
    for arg in args:
        print(arg)

# Função de Cadastro,  Cadastra um contato com id, nome, atividade e telefone. Armazena em um dicionário e copia para lista_contatos.
def cadastrar_contatos(id):
    mostrar_mensagens(*mensagem["Registrar"])
    print(f"Seu Id: {id}")
    nome = input("Por favor, entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do Contato: ")

    # Dicionário com os dados contato
    contato = {"id": id, "nome": nome, "atividade": atividade, "telefone": telefone}

    # Adiciona uma cópia do dicionário à lista principal
    lista_contatos.append(contato.copy())


# Função de Consulta dos contatos dentro da lista
def consultar_contatos():

    while True:
        mostrar_mensagens(*mensagem["Consultar"])
        consultar = input(">> ")

        if consultar == "1":
            for contato in lista_contatos:
                print(
                    f"\nId: {contato['id']}  \nNome: {contato['nome']}  \nAtividade: {contato['atividade']}  \nTelefone: {contato['telefone']}\n\n"
                )
            if not lista_contatos:
                print("Nenhum contato cadastrado.")

        elif consultar == "2":
            try:
                id_busca = int(input("Digite o Id do contato: "))
                encontrado = False
                for contato in lista_contatos:
                    if contato["id"] == id_busca:
                        print(
                            f"\nContato encontrado: Id: {contato['id']} \nNome: {contato['nome']} \nAtividade: {contato['atividade']} \nTelefone: {contato['telefone']}\n\n"
                        )
                        encontrado = True
                        break
                if not encontrado:
                    print("Id não encontrado.")

            except ValueError:
                print("Digite um número válido para o Id.")

        elif consultar == "3":
            atividade_busca = input("Digite a atividade: ").strip().lower()
            encontrados = [
                c for c in lista_contatos if c["atividade"].lower() == atividade_busca
            ]
            if encontrados:
                for c in encontrados:
                    print(
                        f"\nId: {c['id']} \nNome: {c['nome']} \nTelefone: {c['telefone']}\n\n"
                    )
            else:
                print("Nenhum contato encontrado com essa atividade.")

        elif consultar == "4":
            print("Retornando ao menu principal...\n")
            return

        else:
            print("Opção inválida! Tente novamente.")


# Função que remove os contatos de dentro da lista
def remover_contato():

    while True:
        mostrar_mensagens(*mensagem["Remover"])
        try:
            id_remove = int(input("Digite o Id do contato a ser removido: "))
            for contato in lista_contatos:
                if contato["id"] == id_remove:
                    lista_contatos.remove(contato)
                    print(f"Contato {id_remove} removido com sucesso!\n")
                    return
            print("Id inválido, tente novamente.\n")

        except ValueError:
            print("Digite um número válido para o Id.\n")


# Menu principal
while True:

    mostrar_mensagens(*mensagem["Principal"])
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
                cadastrar_contatos(id_global)
                id_global += 1 # incrementa +1 ao id, a cada novo cadastro             
        case "2":
                consultar_contatos()
        case "3":
                remover_contato()
        case "4":
                print("Programa encerrado. Até logo!")
                break
        case _:
                print("Opção inválida! Escolha entre 1 e 4.\n")


