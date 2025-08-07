# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

a = float(input("Primeira reta: "))
b = float(input("Segunda reta: "))
c = float(input("Terceira reta: "))

cores = {"limpa": "\033[m",
         "branco": "\033[0;30m",
         "vermelho":"\033[0;31m",
         "verde":"\033[0;32m",
         "amarelo":"\033[0;33m",
         "azul":"\033[0;34m",
         "roxo":"\033[0;35m",
         "ciano":"\033[0;36m",
         "cinza":"\033[0;37m",
         "back_branco":"\033[0;40m",
         "back_vermelho":"\033[0;41m",
         "back_verde":"\033[0;42m",
         "back_amarelo":"\033[0;43m",
         "back_azul":"\033[0;44m",
         "back_roxo":"\033[0;45m",
         "back_ciano":"\033[0;46m",
         "back_cinza":"\033[0;47m"
         }

if (a+b > c) and (a+c > b) and (b+c > a):
    if (a != b != c != a):
        print("As retas de comprimento \033[1;32m{}\033[m, \033[1;32m{}\033[m e \033[1;32m{}\033[m podem formar um \033[1;32mTRIÂNGULO ESCALENO!\033[m".format(a,b,c))
    elif ((a == b) and (a != c))  or ((a == c) and (a !=b )) or ((b == c) and b != a):
        print("As retas de comprimento \033[1;32m{}\033[m, \033[1;32m{}\033[m e \033[1;32m{}\033[m podem formar um \033[1;32mTRIÂNGULO ISÓSCELES!\033[m".format(a,b,c))
    elif (a == b == c):
        print("As retas de comprimento \033[1;32m{}\033[m, \033[1;32m{}\033[m e \033[1;32m{}\033[m podem formar um \033[1;32mTRIÂNGULO EQUILÁTERO!\033[m".format(a,b,c))
else:
    print("As retas de comprimento \033[1;31m{}\033[m, \033[1;31m{}\033[m e \033[1;31m{}\033[m, \033[1;31mNÃO PODEM FORMAR UM TRIÂNGULO\033[m".format(a,b,c))