from math import sqrt

cateto_oposto = float(input("Digite o Cateto Oposto do triângulo: "))
cateto_adjacente = float(input("Digite o Cateto Adjacente do triângulo: "))

hipotenusa = sqrt((cateto_adjacente**2)+(cateto_oposto**2))

print("O valor da hipotenusa é {:.2f}".format(hipotenusa))

