# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do carro em KM/H? "))

if velocidade > 80:
    km = 7.00
    multa = (velocidade - 80) * km
    print("Você foi multado por passar a {:.0f}KM/h acima do limite de velocidade.".format(velocidade-80))
    print("O valor da multa é R$ {:.2f}!".format(multa))

else:
    print("Tenha um bom dia, dirija com segurança!")