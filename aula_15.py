# Listas em Python

cursos = ['Python', 'Git', 'Design', 'JavaScript']

print(cursos)
print(cursos[1])  # Imprime o segundo elemento da lista



cursos[1] = "GitHub e Git"  # Modifica o segundo elemento da lista
print(cursos)

cursos.append("Dados") # Adiciona o elemento "Dados" ao final da lista
print(cursos)


cursos.remove("Design")  # Remove o elemento "Design" da lista
cursos.pop(0)  # Remove o primeiro elemento da lista
print(cursos)