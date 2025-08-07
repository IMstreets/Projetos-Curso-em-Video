lista = []
soma = 0
contador = 0
for i in range(0,6):
    entrada = int(input("Digite {}º valor inteiro: ".format(i+1)))
    lista.append(entrada)
for numero in lista:
    if numero%2 == 0:
        soma += numero
        contador += 1
print("A soma desses {} valores pares é {}".format(contador,soma))