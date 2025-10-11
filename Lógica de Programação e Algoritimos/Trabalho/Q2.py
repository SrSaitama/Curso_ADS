print('-'*10, ' Bem-vindo a Pizzaria do Bruno Eliakim ', '-'*10)
print('-'*25, 'Cardápio', '-'*25)
print('-'*60)

dados = [
    ["P", "R$ 30.00", "R$ 34.00"],
    ["M", "R$ 45.00", "R$ 48.00"],
    ["G", "R$ 60.00", "R$ 66.00"]
]

print(f"---| {'Tamanho':<10} | {'Pizza Salgada (PS)':<10} | {'Pizza Doce (PD)':<10} |---")

for linha in dados:
    tamanho, salgada, doce = linha
    print(f"---| {tamanho:<10} | {salgada:<18} | {doce:<15} |---")

print("-" * 60) # Linha inferior da tabela

while True:
    sabor = input("Entre com o sabor desejado (PS/PD): ").upper().strip()
    if sabor in ("PD", "PS"):
        break
    else:
        print("Sabor inválida, tente novamente.")

while True:
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper().strip()
    if tamanho in ("P", "M", "G"):
        break
    else:
        print("Tamanho inválida, tente novamente.")

print(f"{sabor}")
print(f"{tamanho}")

if(sabor == "PD"):
    if(tamanho == "P"):
        valor = 34
    elif(tamanho == "M"):
        valor = 48
    else:
        valor = 66
else:
    if(tamanho == "P"):
        valor = 30
    elif(tamanho == "M"):
        valor = 45
    else:
        valor = 60

print(f"{valor}")










""""
opc = str(input("Deseja mais alguma coisa? (S/N) ")).upper().strip()

if (opc == "S"):

        while True:
            sabor = input("Entre com o sabor desejado (PS/PD): ").upper().strip()
            if sabor in ("PD", "PS"):
                if(sabor == "PD"):
                    if(tamanho == "P"):
                        valor = 34
                    elif(tamanho == "M"):
                        valor = 48
                    else:
                        valor = 66
                else:
                    if(tamanho == "P"):
                        valor = 30
                    elif(tamanho == "M"):
                        valor = 45
                    else:
                        valor = 60

            else:
                print("Sabor inválida, tente novamente.")

            while True:
                tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper().strip()
                if tamanho in ("P", "M", "G"):
                    continue
                else:
                    print("Tamanho inválida, tente novamente.")

            print(f"{sabor}")
            print(f"{tamanho}")

            
            print(f"{valor}")
elif(opc == "N"):
    print(f"O valor total a ser pago: R$ {valor:.2f}")
else:
    print("Opção inválida, tente novamente.")
    
"""