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
    print("As retas de comprimento {}{}{}, {}{}{} e {}{}{} podem formar um triângulo!".format(cores["vermelho"],a,cores["limpa"],cores["back_ciano"],b,cores["limpa"],cores["back_verde"],c,cores["limpa"]))
else:
    print("As retas de comprimento \033[31m{}\033[m,, \033[32m{}\033[m, e \033[33m{}\033[m, NÃO PODEM FORMAR UM TRIÂNGULO".format(a,b,c))