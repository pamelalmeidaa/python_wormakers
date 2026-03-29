


nome = input("Qual é o seu nome? ")
idade = int(input("Qual é o sua idade? ")) # int() para converter a string em um número inteiro
ano = int(input("Qual é o ano atual? "))
altura = float(input("Qual é a sua altura? ")) # float() para converter a string em um número decimal (ponto flutuante)

print(f"Olá, {nome}! Seja bem vinda ao mundo Python!") # f-string para formatar a string com a variável nome

ano_nascimento = ano - idade   # Cálculo do ano de nascimento subtraindo a idade do ano atual
idade_futura = idade + 5 # Cálculo da idade futura somando 5 anos à idade atual
idade_dobro = idade * 2 # Cálculo da idade dobro multiplicando a idade por 2
idade_quadrado = idade ** 2 # Cálculo da idade quadrado elevando a idade ao quadrado
maior_idade = idade >= 18 # Cálculo se a idade é maior ou igual a 18
altura_160 = altura >= 1.60 # Cálculo se a altura é maior ou igual a 1.60