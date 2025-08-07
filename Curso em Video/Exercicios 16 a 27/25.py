#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input("Digite seu nome: ")

nome = nome.lower()

if nome.find("silva") == -1:
    print(False)

else:
    print(True)
