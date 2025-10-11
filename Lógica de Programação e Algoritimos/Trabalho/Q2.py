print("-" * 10, " Bem-vindo a Pizzaria do Bruno Eliakim ", "-" * 10)
print("-" * 25, "Cardápio", "-" * 25)
print("-" * 60)

dados = [
    ["P", "R$ 30.00", "R$ 34.00"],
    ["M", "R$ 45.00", "R$ 48.00"],
    ["G", "R$ 60.00", "R$ 66.00"],
]

print(
    f"---| {'Tamanho':<10} | {'Pizza Salgada (PS)':<10} | {'Pizza Doce (PD)':<10} |---"
)

for linha in dados:
    tamanho, salgada, doce = linha
    print(f"---| {tamanho:<10} | {salgada:<18} | {doce:<15} |---")

print("-" * 60)

valor_total = 0
step = 1

while True:

    if step == 1:
        sabor = input("Entre com o sabor desejado (PS/PD): ").upper().strip()
        if sabor not in ("PD", "PS"):
            print("Sabor inválida, tente novamente.")
            continue
        step += 1

    if step == 2:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper().strip()
        if tamanho not in ("P", "M", "G"):
            print("Tamanho inválida, tente novamente.")
            continue
        step += 1

    if sabor == "PD":
        if tamanho == "P":
            valor_total += 34
        elif tamanho == "M":
            valor_total += 48
        else:
            valor_total = 66
    else:
        if tamanho == "P":
            valor_total += 30
        elif tamanho == "M":
            valor_total += 45
        else:
            valor_total += 60

    print(f"O valor total ate agora é: {valor_total}")
    resposta = input("Deseja pedir mais alguma coisa? (sim/não): ")

    if resposta.lower() == "não":
        print(f"total a pagar: {valor_total}")
        break
    elif resposta.lower() == "sim":
        step = 1
        continue
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

