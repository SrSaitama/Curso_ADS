print("Bem vindo a Madeireira do Lenhador Bruno Eliakim\n")

# Função: escolha_tipo()
def escolha_tipo():
    global tipoMadeira

#     Pergunta o tipo de madeira desejado e retorna o valor da tora. Repete se o usuário digitar uma opção inválida.
    while True:
        tipoMadeira = input("Entre com o Tipo de Madeira desejado\n"
        "PIN - Tora de Pinheiro\n"
        "PER - Tora de Peroba\n"
        "MOG - Tora de Mogno\n"
        "IPE - Tora de Ipê\n"
        "IMB - Tora de Imbuia\n>>").upper().strip()
        if tipoMadeira not in ("PIN", "PER", "MOG", "IPE", "IMB"):
            print("Escolha inválida, entre com o modelo novamente!\n")
            continue
        else:
            if(tipoMadeira == "PIN"):
                    return 150.40
            elif(tipoMadeira == "PER"):
                return 170.20
            elif(tipoMadeira == "MOG"):
                return 190.90
            elif(tipoMadeira == "IPE"):
                return 210.10
            else:
                return 220.70


# Função: qtd_toras()
def qtd_toras():
#    Pergunta a quantidade de toras desejada e retorna a quantidade e o valor do desconto.
    while True:

#    Usa try/except para tratar erros de entrada.
        try:
            num_toras = int(input("Entre com a quantidade de toras (m³) desejado: "))
            
            if (num_toras > 2000):
                print("Não aceitamos pedidos com essa quantidade de toras!\n"
                "Por favor, entre com a quantidade novamente.\n")
                continue
            elif(num_toras < 0):
                print("Informe um valor positivo!")
                continue

            # Define desconto conforme a faixa
            if(num_toras < 100):
                desconto = 0/100
            elif(num_toras < 500):
                desconto = 4/100
            elif(num_toras < 1000):
                desconto = 9/100
            else:
                desconto = 16/100

            return num_toras, desconto

        except ValueError:
            print("Digite um valor positivo!")


# Função: transporte()
def transporte():
    while True:
        tipo_transporte = input("\nEntre com o Tipo de Transporte desejado\n"
        "1 - Transporte Rodoviário  - R$ 1000.00\n"
        "2 - Transporte Ferroviário - R$ 2000.00\n"
        "3 - Transporte Hidroviário - R$ 2500.00\n>>").upper().strip()
             
        if(tipo_transporte == "1"):
            return 1000
        elif(tipo_transporte == "2"):
            return 2000
        elif(tipo_transporte == "3"):
            return 2500
        else:
            print("Escolha inválida!\n")

     
# Código principal (main)
try:
    # Chama as funções e recebe os valores retornados
    valor_tora = escolha_tipo()
    qtd, desconto = qtd_toras()
    valor_transporte = transporte()

    # Calcula o total com desconto aplicado e transporte incluso
    total = ((valor_tora * qtd) * (1 - desconto)) + valor_transporte

    # Exibe o resultado final
    print(f"Total: R$ {total:.2f}")

except Exception as e:
    # [EXIGÊNCIA DE CÓDIGO 6 de 7]
    print(f"Ocorreu um erro inesperado: {e}")


