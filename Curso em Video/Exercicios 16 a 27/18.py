from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo: "))


seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("Para o angulo {} nós temos: \nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(angulo,seno,cosseno,tangente))