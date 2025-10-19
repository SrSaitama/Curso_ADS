lista_contatos = []

state = {"opcao": "0", "messageSuccess": "", "messageError": ""}


def draw_lines(n):
    lines = "-" * n
    return lines


messages = {
    "main": [
        "\n",
        draw_lines(50),
        f"{draw_lines(15)} MENU PRINCIPAL {draw_lines(15)}",
        "1 - Cadastrar Contato",
        "2 - Consultar Contato",
        "3 - Remover Contato",
        "4 - Sair",
    ],
    "register": [
        draw_lines(50),
        f"{draw_lines(15)} MENU CADASTRAR CONTATO {draw_lines(15)}",
    ],
    "consultar": [
        draw_lines(50),
        f"{draw_lines(15)} MENU CONSULTAR CONTATOS {draw_lines(15)}",
        "Qual opção deseja: ",
        "1 - Consultar Todos",
        "2 - Consultar por Id",
        "3 - Consultar por Setor",
        "4 - Retomar ao menu",
    ],
    "remover": [
        draw_lines(50),
        f"{draw_lines(15)} MENU REMOVER CONTATO {draw_lines(15)}",
    ],
}


def display_messages(*args):
    for arg in args:
        print(arg)


def cadastrar_contatos(id):
    nome = input("Por favor, entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do Contato: ")

    contato = {"id": id, "nome": nome, "atividade": atividade, "telefone": telefone}

    lista_contatos.append(contato)


def consultar_contatos():
    consultar = input(">> ")

    if consultar == "1":
        draw_lines(50)
        for contato in lista_contatos:
            display_messages(
                f"Id: {contato['id']}  \nNome: {contato['nome']}  \nAtividade: {contato['atividade']}  \nTelefone: {contato['telefone']}\n\n"
            )
        if not lista_contatos:
            state["messageError"] = "Nenhum contato cadastrado."
            return None

    elif consultar == "2":
        try:
            id_busca = int(input("Digite o Id do contato: "))
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == id_busca:
                    display_messages(
                        f"\nContato encontrado: Id: {contato['id']} \nNome: {contato['nome']} \nAtividade: {contato['atividade']} \nTelefone: {contato['telefone']}\n\n"
                    )
                    encontrado = True
            if not encontrado:
                state["messageError"] = "Id não encontrado."
                return None

        except ValueError:
            state["messageError"] = "Digite um id valido"
            return None

    elif consultar == "3":
        atividade_busca = input("Digite a atividade: ").strip().lower()
        encontrados = [
            c for c in lista_contatos if c["atividade"].lower() == atividade_busca
        ]
        if encontrados:
            # print(f"\n--- Contatos com atividade '{atividade_busca}' ---")
            for c in encontrados:
                display_messages(
                    f"Id: {c['id']} \nNome: {c['nome']} \nTelefone: {c['telefone']}\n\n"
                )
        else:
            state["messageError"] = "Nenhum contato encontrado com essa atividade."
            return None

    elif consultar == "4":
        display_messages("Retornando ao menu principal...\n")
        return True

    else:
        state["messageError"] = "Opção inválida! Tente novamente."
        return None


def remover_contato():
    try:
        id_remove = int(input("Digite o Id do contato a ser removido: "))
        for contato in lista_contatos:
            if contato["id"] == id_remove:
                lista_contatos.remove(contato)
                print(f"Contato {id_remove} removido com sucesso!\n")
                return True

        state["messageError"] = "Id inválido, tente novamente."
        return None

    except ValueError:
        state["messageError"] = "Digite um número válido para o Id."
        return None


def run():
    global state
    count_id = 0

    while True:
        match state["opcao"]:
            case "0":
                display_messages(*messages["main"])
                state["opcao"] = input("Ecolha uma opção: \n")

                continue
            case "1":
                count_id += 1
                display_messages(*messages["register"])

                cadastrar_contatos(count_id)

                state["opcao"] = "0"
                continue
            case "2":
                display_messages(*messages["consultar"])

                if consultar_contatos():
                    state["opcao"] = "0"
                else:
                    display_messages(state["messageError"])
                    continue

            case "3":
                display_messages(*messages["remover"])

                if remover_contato():
                    state["opcao"] = "0"
                else:
                    display_messages(state["messageError"])
                    continue

            case "4":
                display_messages("Programa encerrado. Até logo!")
                break
            case _:
                display_messages("Opção inválida! Escolha entre 1 e 4.\n")


def start():
    display_messages("Bem vindo a Lista de Contatos do Bruno Eliakim")
    run()


start()
