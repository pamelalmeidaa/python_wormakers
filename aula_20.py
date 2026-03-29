# Tratamento de Erros

#try:
"""    numero = int(input("digite um número:"))
    resultado =10/ numero

except ZeroDivisionError:
    print("Não é possível / por ZERO!")


except ValueError:
    print("Digite somente número")

else:
        print(f"Resultado: {resultado}")"""


try:
    arquivo = open("dados.txt", mode="r")
    conteudo = arquivo.read()


except FileExistsError:
    print("Arquivo não encontrado!")


finally:
    print("Operação finalizada!")