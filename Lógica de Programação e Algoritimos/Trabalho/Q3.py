print("Bem vindo a Madeireira do Lenhador Bruno Eliakim\n")

global valor_tora 
global tipoMadeira
global desconto
global num_toras


def escolha_tipo():
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
        res = print(f"O valor por m³ é: {valor_tora:.2f}\n")
        break

    return res



def qtd_toras():
    desconto = 0
    while True:
        num_toras = input("Entre com a quantidade de toras (m³) desejado: ").upper().strip()
        if (num_toras <= 0 or num_toras > 2000):
            print("Não aceitamos pedidos com essa quantidade de toras!\n"
            "Por favor, entre com a quantidade novamente.\n")
            continue
        elif(num_toras < 100):
            desconto == (0/100)
        elif(num_toras >= 100 and num_toras < 500):
            desconto == (4/100)
        elif(num_toras >= 500 and num_toras < 1000):
            desconto == (9/100)
        elif(num_toras >= 1000 and num_toras < 2000):
            desconto == (16/100)
        else:
            print("Informe um valor válido!")
            continue

        res = print(f"a quantidade de toras é: {num_toras:.2f}"
                    "o valor do desconto é: {desconto:.2f}\n")
        break

    return res

def transporte():
    valor_transporte
    while True:
        tipo_transporte = input("Entre com o Tipo de Madeira desejado\n"
        "1 - Transporte Rodoviário  - R$ 1000.00\n"
        "2 - Transporte Ferroviário - R$ 2000.00\n"
        "3 - Transporte Hidroviário - R$ 2500.00\n>>").upper().strip()
        
        if tipo_transporte not in ("1", "2", "3"):
            print("Escolha inválida!\n")
            continue
        elif(tipo_transporte == "1"):
            valor_transporte = 1000
        elif(tipo_transporte == "2"):
            valor_transporte = 2000
        else:
            valor_transporte = 2500


        
        total = ((tipoMadeira * num_toras)*(1-desconto)) + tipo_transporte

        res = print(f"{total:.2f}")
        break

    return res


escolha_tipo()
qtd_toras()
transporte()

