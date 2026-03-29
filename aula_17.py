# Dicionairos de Dados em Python

escola = [
    {
        "nome": "João",
        "idade": 15,        
        "curso": "Python",
        "studo": True
    },
    
    {
        "nome": "Maria",
        "idade": 16,        
        "curso": "C#",
        "studo": False
    },

    {        "nome": "Pedro",
        "idade": 14,
        "curso": "Dados",
        "studo": True
    }
]

# print(escola)

for aluna in escola:
    print(f"Nome:{aluna['nome']}")
    print(f"Curso:{aluna['curso']}")
    print("-"*20)

