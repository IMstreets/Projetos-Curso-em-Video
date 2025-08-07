# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
cont = 0
for i in range(1,(int(numero**(1/2))+1)):
    if numero % i == 0:
        if i == 1:
            continue
        else:
            print("Não é primo")
            cont += 1
            break
if cont == 0:
    print("É primo")