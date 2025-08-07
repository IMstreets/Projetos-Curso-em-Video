#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

primeiro = int(input("Digite o primeiro Numero: "))
segundo = int(input("Digite o segundo Numero: "))
terceiro = int(input("Digite o terceiro Numero: "))

lista = [primeiro,segundo,terceiro]
lista = sorted(lista)
print("O menor numero é {} e o maior numero é {}".format(lista[0],lista[2]))