# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
# aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela 
# aparece a última vez.

frase = str(input("Digite sua frase: ").strip()).lower()

contagem = frase.count("a")

primeiro = (frase.find("a"))+1
ultimo = (frase.rfind("a"))+1

print("A letra A aparece {} vezes na frase.".format(contagem))
print("A primeira letra A apareceu na posição {}".format(primeiro))
print("A última letra A apareceu na posição {}".format(ultimo))