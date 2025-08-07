# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import math

print("-="*20)
numero = int(input("Digite um número de 0 a 9999: "))
print("-="*20)

#3254

if 0 <= numero <= 9999:
    
    milhar = math.floor(numero/1000)
    centena = math.floor((numero - (milhar*1000))/100)
    dezena = math.floor((numero - (milhar*1000) - (centena*100))/10)
    unidade = math.floor((numero - (milhar*1000) - (centena*100)) - (dezena*10))

    print("-="*20)
    print("""O numero tem: 
          Unidade: {}
          Dezena: {}
          Centena: {}
          Milhar: {}""".format(unidade,dezena,centena,milhar))
    print("-="*20)
    
else:
    print("-="*20)
    print("O numero não é válido")
    print("-="*20)