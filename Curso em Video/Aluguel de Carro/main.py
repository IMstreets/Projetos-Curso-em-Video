# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
# que o carro custa R$60 por dia e R$0,15 por Km rodado.
import math
import CTkinter 
try:
    print("-=-=-=-=-="*5)
    km_rodados = float(input("Quantidade de KMs rodados: "))
    dias = int(input("Quantidades de dias alugados: "))
    total = (60*dias) + (km_rodados*0.15)
    print(f"O preço a se pagar pelo aluguel é R$ {total:.2f}")
    print("-=-=-=-=-="*5)

except:
    print("Entrada não válida")