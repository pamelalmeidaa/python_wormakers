#Funções


def saudacao(nome, estado):
    print(f"{nome}, seja bem-vindo. Muito bom ver alguem de {estado}")


def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

def verificar_idade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."
    
print(verificar_idade(18))