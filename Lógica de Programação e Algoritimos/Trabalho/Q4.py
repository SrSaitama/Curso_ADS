lista_contatos = []

def draw_lines(n):
    lines = "-" * n
    return lines


messages = {
    "Principal": [
        draw_lines(50),
        f"{draw_lines(15)} MENU PRINCIPAL {draw_lines(15)}",
        "1 - Cadastrar Contato",
        "2 - Consultar Contato",
        "3 - Remover Contato",
        "4 - Sair",
    ],
    "Registrar": [
        draw_lines(50),
        f"{draw_lines(15)} MENU CADASTRAR CONTATO {draw_lines(15)}",
    ],
    "Consultar":[
        draw_lines(50),
        f"{draw_lines(15)} MENU CONSULTAR CONTATOS {draw_lines(15)}",
            "Qual opção deseja:",
            "1 - Consultar Todos",
            "2 - Consultar por Id",
            "3 - Consultar por Setor",
            "4 - Retomar ao menu",
    ],
    "Remover":[
        draw_lines(50),
        f"{draw_lines(15)} MENU REMOVER CONTATO {draw_lines(15)}",
    ],
}


def display_messages(*args):
    for arg in args:
        print(arg)


def cadastrar_contatos(id):
    display_messages(*messages["Registrar"])
    print(f"Seu Id: {id}")
    nome = input("Por favor, entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do Contato: ")

    contato = {"id": id, "nome": nome, "atividade": atividade, "telefone": telefone}

    lista_contatos.append(contato.copy)


def consultar_contatos():

    while True:
        display_messages(*messages["Consultar"])
        consultar = input(">> ")

        if consultar == "1":
            draw_lines(15)
            for contato in lista_contatos:
                print(
                    f"Id: {contato['id']}  \nNome: {contato['nome']}  \nAtividade: {contato['atividade']}  \nTelefone: {contato['telefone']}\n\n"
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
                # print(f"\n--- Contatos com atividade '{atividade_busca}' ---")
                for c in encontrados:
                    print(
                        f"Id: {c['id']} \nNome: {c['nome']} \nTelefone: {c['telefone']}\n\n"
                    )
            else:
                print("Nenhum contato encontrado com essa atividade.")

        elif consultar == "4":
            print("Retornando ao menu principal...\n")
            return

        else:
            print("Opção inválida! Tente novamente.")


def remover_contato():

    while True:
        display_messages(*messages["Remover"])
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

def run():
    id_global = 5558147

    while True:

        display_messages(*messages["Principal"])
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                id_global += 1
                cadastrar_contatos(id_global)
            case "2":
                consultar_contatos()
            case "3":
                remover_contato()
            case "4":
                print("Programa encerrado. Até logo!")
                break
            case _:
                print("Opção inválida! Escolha entre 1 e 4.\n")


def start():
    print("Bem vindo a Lista de Contatos do Bruno Eliakim")
    run()


start()

