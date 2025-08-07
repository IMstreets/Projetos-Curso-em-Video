# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de 
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
# mostre a ordem sorteada.

import random

primeiro = input("Primeiro Aluno: ")
segundo = input("Segundo Aluno: ")
terceiro = input("Terceiro Aluno: ")
quarto = input("Quarto Aluno: ")

alunos = [primeiro, segundo, terceiro, quarto]

random.shuffle(alunos)

print("A ordem de apresentação será:")
print(alunos)