# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas e minúsculas.
# 2) Quantas letras ao todo (sem considerar espaços).
# 3) Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome completo: ")

print("Maiúsculo: {}".format(nome.upper()))
print("Minúsculo: {}".format(nome.lower()))
tamanho = nome.replace(" ","")
print("Seu nome tem {} letras".format(len(tamanho)))
primeiro_nome = nome.split()
print("Seu primeiro nome tem {} letras.".format(len(primeiro_nome[0])))