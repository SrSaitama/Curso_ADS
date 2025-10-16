print("Bem vindo a Madeireira do Lenhador Bruno Eliakim\n")

valor_tora = None
tipoMadeira = None
desconto = None
num_toras = None


def escolha_tipo():
    global tipoMadeira
    global valor_tora
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
                valor_tora = 150.40
            elif(tipoMadeira == "PER"):
                valor_tora = 170.20
            elif(tipoMadeira == "MOG"):
                valor_tora = 190.90
            elif(tipoMadeira == "IPE"):
                valor_tora = 210.10
            else:
                valor_tora = 220.70
        break
    return 



def qtd_toras():
    global num_toras
    global desconto
    while True:
        try:
            num_toras = int(input("Entre com a quantidade de toras (m³) desejado: "))
            
            if (num_toras > 2000):
                print("Não aceitamos pedidos com essa quantidade de toras!\n"
                "Por favor, entre com a quantidade novamente.\n")
                continue
            elif(num_toras < 0):
                print("Informe um valor positivo!")
                continue

            if(num_toras < 100):
                desconto = (0/100)
            elif(num_toras < 500):
                desconto = (4/100)
            elif(num_toras < 1000):
                desconto = (9/100)
            else:
                desconto = (16/100)

            return num_toras, desconto

        except ValueError:
            print("Digite um valor numerico!")



def transporte():
    while True:
        tipo_transporte = input("\nEntre com o Tipo de Transporte desejado\n"
        "1 - Transporte Rodoviário  - R$ 1000.00\n"
        "2 - Transporte Ferroviário - R$ 2000.00\n"
        "3 - Transporte Hidroviário - R$ 2500.00\n>>").upper().strip()
             
        if(tipo_transporte == "1"):
            valor_transporte = 1000
        elif(tipo_transporte == "2"):
            valor_transporte = 2000
        elif(tipo_transporte == "3"):
            valor_transporte = 2500
        else:
            print("Escolha inválida!\n")
            continue
      
        total = ((valor_tora * num_toras)*(1-desconto)) + valor_transporte

        res = print(f"{total:.2f}")
        break

    return res


escolha_tipo()
qtd_toras()
transporte()

