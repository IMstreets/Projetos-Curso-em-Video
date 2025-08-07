#Faça um programa que 
# leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro nome
# o último nome separadamente.

nome = str(input("Digite o seu nome completo: ")).strip().title()

nome_lst = nome.split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome_lst[0]))
print("Seu ultimo nome é {}".format(nome_lst[-1]))