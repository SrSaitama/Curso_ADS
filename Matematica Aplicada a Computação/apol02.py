#Aritmétrica de ponto flutuante
#Soma
a = 7.0102e+05
b = 2.1233e+03

c = a + b
print('%.10e' % c)

# Imprimindo o resultado em formato decimal
print(f"O resultado em formato decimal é: {c}")

# Imprimindo o resultado em notação científica formatada
print(f"O resultado em notação científica é: {c:e}")

# Imprimindo o resultado formatado com precisão específica (10 casas decimais)
print(f"O resultado formatado é: {c:.10f}")

#Subtração:
a = 7.0102e5
b = 2.1233e3 # ou 0.021233e5

c = a - b
print('%.10e' % c)

