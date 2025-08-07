# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

primeiro = input("Primeiro Aluno: ")
segundo = input("Segundo Aluno: ")
terceiro = input("Terceiro Aluno: ")
quarto = input("Quarto Aluno: ")

alunos = [primeiro, segundo, terceiro, quarto]

print(random.choice(alunos))