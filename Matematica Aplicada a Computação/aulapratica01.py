# Q1 - a=F, b=V, c=V, d=F, e=F, f=F, g=V

# Q2 - a=V, b=V, c=F, d=V, e=V, f=F, g=V
""""
p=True
q=True
r=False
#a
print(p or q)
#b
print(p or r)
#c
print(q and r)
#d
print(not(q and r))
#e
print(q or r)
#f
print(not(p))
#g
print(not(p and r)) """

# Q3 - 
"""
senha = int(input("Digite a senha: "))
if senha==705080:
   print("Acesso Liberado")
else:
  print("Acesso negado") """
# Q4 - 
"""
renda_mensal = float(input("Informe sua renda mensal liquida: "))
opc = input("Tem financiamentos ou empréstimos? (s/n)").lower().strip()
if opc=="s":
    porcentagem = float(input("Quanto porcento é descontado da renda mensal liquida? %"))

    desconto = renda_mensal * (porcentagem/100)
    print(desconto)
    nova_mensal = renda_mensal - desconto

    if nova_mensal>=8000:
        print("Empréstimo Aprovado!")
    else:
        print("Empréstimo Negado!")

elif opc=="n":
    if renda_mensal>=8000:
        print("Empréstimo Aprovado!")
    else:
        print("Empréstimo Negado!")

else:
    print("Valor invalido!") """

# Q5 - 
"""
atv01 = float(input("Informe sua nota da 1ª atividade: "))
atv02 = float(input("Informe sua nota da 2ª atividade: "))
prova = float(input("Informe a nota da prova objetiva: "))

soma = atv01 + atv02 + prova

if soma<30:
    print("Reprovado!")
elif soma>=30 and soma<70:
    print("Em exame final!")
else:
    print("Aprovado!") """

# Q6 - 
""""
senha1 = 705080
senha2 = 999999

senha = int(input("Informe a senha: "))

if senha==senha1 or senha==senha2:
    print("Entrada liberada!")
else:
    print("Entrada não autorizada!") """

# Q7 - Verdade (Vera Fisher)

# Q8 - Falso (Filhos Gêmeos Verdade)
