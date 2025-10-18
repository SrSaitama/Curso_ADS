print("Bem vindo a Lista de Contatos do Bruno Eliakim")

lista_contatos = []
id_global = 5558147


def cadastrar_contatos(id):

    print("\n","-"*50)
    print("-"*15, " MENU CADASTRAR CONTATO ", "-"*15)
    id = input("Id do Contato: ")
    nome = input("Por favor, entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do Contato: ")

    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    lista_contatos.append(contato.copy())

def consultar_contatos():

    while True:
        print("\n","-"*54)
        print("-"*15, " MENU CONSULTAR CONTATOS ", "-"*15)
        print("Qual opção deseja: \n" 
        "1 - Consultar Todos\n" 
        "2 - Consultar por Id\n" 
        "3 - Consultar por Setor\n" 
        "4 - Retomar ao menu\n")

        consultar = input(">> ")

        if (consultar == "1"):
            print("-"*25)
            for contato in lista_contatos:
                print(f"Id: {contato['id']}  \nNome: {contato['nome']}  \nAtividade: {contato['atividade']}  \nTelefone: {contato['telefone']}\n\n")
            if not lista_contatos:
                print("Nenhum contato cadastrado.")

    
        elif (consultar == "2"):
            try:
                id_busca = int(input("Digite o Id do contato: "))
                encontrado = False
                for contato in lista_contatos:
                    if contato["id"] == id_busca:
                        print(f"\nContato encontrado: Id: {contato['id']} \nNome: {contato['nome']} \nAtividade: {contato['atividade']} \nTelefone: {contato['telefone']}\n\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("Id não encontrado.")

            except ValueError:
                print("Digite um número válido para o Id.")



        elif (consultar == "3"):
            atividade_busca = input("Digite a atividade: ").strip().lower()
            encontrados = [c for c in lista_contatos if c["atividade"].lower() == atividade_busca]
            if encontrados:
                #print(f"\n--- Contatos com atividade '{atividade_busca}' ---")
                for c in encontrados:
                    print(f"Id: {c['id']} \nNome: {c['nome']} \nTelefone: {c['telefone']}\n\n")
            else:
                print("Nenhum contato encontrado com essa atividade.")



        elif (consultar == "4"):
            print("Retornando ao menu principal...\n")
            return

        else:
            print("Opção inválida! Tente novamente.")


def remover_contato():
    
    print("\n","-"*54)
    print("-"*15, " MENU REMOVER CONTATO ", "-"*15)

    while True:
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



while True:
    print("\n","-"*54)
    print("-"*15, " MENU PRINCIPAL ", "-"*15)
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato")
    print("3 - Remover Contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_contatos(id_global)
        id_global += 1  

    elif opcao == "2":
        consultar_contatos()

    elif opcao == "3":
        remover_contato()

    elif opcao == "4":
        print("Programa encerrado. Até logo!")
        break

    else:
        print("Opção inválida! Escolha entre 1 e 4.\n")