print("-" * 10, " Bem-vindo a Pizzaria do Bruno Eliakim ", "-" * 10)
print("-" * 25, "Cardápio", "-" * 25)
print("-" * 60)

# Criação de uma lista menu, onde ficaram os preços e tamanhos.
menu = [
    ["P", "R$ 30.00", "R$ 34.00"],
    ["M", "R$ 45.00", "R$ 48.00"],
    ["G", "R$ 60.00", "R$ 66.00"],
]

print(
    f"---| {'Tamanho':<10} | {'Pizza Salgada (PS)':<10} | {'Pizza Doce (PD)':<10} |---"
)

# Passa por cada linha da lista menu e exibe com os valores formatados.
for linha in menu:
    tamanho, salgada, doce = linha
    print(f"---| {tamanho:<10} | {salgada:<18} | {doce:<15} |---")

print("-" * 60)

# Declaração das variáveis de controle
valor_total = 0
valor_pizza = 0
passo = 1
pizza = " "

# Loop principal do sistema
while True:

    # Passo 1 - Escolha do tipo de pizza
    if passo == 1:
        sabor = input("Entre com o sabor desejado (PS/PD): ").upper().strip()
        if sabor not in ("PD", "PS"):
            print("Sabor inválido, tente novamente.\n")
            continue
        passo += 1

    # Passo 2 - Escolha do tamanho da pizza
    if passo == 2:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper().strip()
        if tamanho not in ("P", "M", "G"):
            print("Tamanho inválido, tente novamente.\n")
            continue
        passo += 1 # Avança para o cálculo do valor da pizza

    # Cálculo do valor da pizza com base no sabor e tamanho
    if sabor == "PD":
        pizza = "Pizza Doce"
        if tamanho == "P":
            valor_pizza = 34
            valor_total += valor_pizza
        elif tamanho == "M":
            valor_pizza = 48
            valor_total += valor_pizza
        else:
            valor_pizza= 66
            valor_total += valor_pizza
    else:
        pizza = "Pizza Salgada"
        if tamanho == "P":
            valor_pizza = 30
            valor_total += valor_pizza
        elif tamanho == "M":
            valor_pizza = 45
            valor_total += valor_pizza
        else:
            valor_pizza = 60
            valor_total += valor_pizza

    #Cola do pedido do cliente
    print(f"Você pediu uma {pizza} no tamanho {tamanho}: R$ {valor_pizza:.2f}\n")

    resposta = input("Deseja mais alguma coisa? (S/N): ")

    # Finaliza o pedido e exibe o total a ser pago
    if resposta.upper().strip() == "N":
        print(f"\nO valor total a ser pago: R$ {valor_total:.2f}")
        break
    elif resposta.upper().strip() == "S":
        passo = 1
        continue
    else:
        print("Resposta inválida. Responda com 'S' ou 'N'.\n")

