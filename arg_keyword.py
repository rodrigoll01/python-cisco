# Argumentos de output
# Prints vazios para melhorar o visual do output.
# Não utilizei o escape \n para ter compreensão
# melhor do código.

print()
print("My name is ", end="")
print("Monty Python.")
print()
print("My name is", "Python.", end=" ")
print("Monty Python.")
print()
print("My name is", "Python.", end="\n")
print("Monty Python.")
print()
# Argumentos com separador e separador vazio
print("My", "name", "is", "Monty", "Python.", sep="-")
print()
print("My", "name", "is", "Monty", "Python.", sep=" ")
print()
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print()
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep=" ", end="\n*")
print()
print("Programming","Essentials","in", sep="***", end="...")
print("Python")
print()
