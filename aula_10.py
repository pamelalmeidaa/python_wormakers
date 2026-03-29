# operações Especiais

# Exemplos de operadores
# += Incremento
# -= Decremento


valorA = int(input("Qual o valor de A? "))
valorB = int(input("Qual o valor de B? "))

valorA += 5
valorB -= 2

print("Valor final de A: ", valorA)
print("Valor final de B: ", valorB)


if valorA % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")