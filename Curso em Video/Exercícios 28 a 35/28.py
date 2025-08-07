#Escreva um programa que faça o computador “pensar” 
# em um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
import pygame

computador = random.randint(0,5)

print("-=-="*15)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-="*15)

player = int(input("Em que número pensei? "))

print("PROCESSANDO...")
time.sleep(2)

if player < 0 and player > 5:
    print("Esse número não é válido.")

elif (player > computador) or (player < computador) :
    print("VOCÊ PERDEU! O numero que eu pensei foi {}!".format(computador))

elif player == computador:
    print("PARABÉNS! Você conseguiu me vencer!")