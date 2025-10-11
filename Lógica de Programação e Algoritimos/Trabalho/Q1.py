
print('Bem vindo ao Sistema do Bruno Eliakim')
      
valorBase = float(input("informe o valor Base do Plano: R$ "))
idade = int(input('Informe a idade do Cliente: '))

valorMensal = 0.0


if (idade>=0 and idade< 19):
    valorMensal = valorBase*(100/100)
    print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}');

elif (idade>=19 and idade< 29):
    valorMensal = valorBase*(150/100)
    print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}');

elif (idade>=29 and idade< 39):
    valorMensal = valorBase*(225/100)
    print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}');

elif (idade>=39 and idade< 49):
    valorMensal = valorBase*(240/100)
    print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}');

elif (idade>=49 and idade< 59):
    valorMensal = valorBase*(350/100)
    print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}');

else:
    valorMensal = valorBase*(600/100)
    print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}');
