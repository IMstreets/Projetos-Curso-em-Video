#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Ano de nascimento: "))
print("""
                 Qual o seu sexo?
                 [ 1 ] Masculino
                 [ 2 ] Feminino
                 
                 """)
sexo = int(input("Digite o número da sua opção: "))
ano_hoje = date.today().year
if sexo == 1:
    print("\033[1;32m-*\033[m"*20)
    print("Você é do sexo MASCULINO" \
    "\nO seu alistamento é OBRIGATÓRIO!")
    print("\033[1;32m-*\033[m"*20)

    if ano_hoje - ano < 18:
        print("""Hoje você tem \033[1;32m{} anos.\033[m
            Ainda faltam \033[1;32m{} anos \033[mpara o alistamento
            Seu alistamento será em \033[1;31m{}.\033[m""".format(ano_hoje-ano,18-(ano_hoje-ano),ano_hoje + 18-(ano_hoje-ano)))
    elif ano_hoje - ano > 18:
        print("""
            Hoje você tem \033[1;32m{} anos.\033[m
            Já deveria ter se alistado a \033[1;32m{} anos \033[m
            Seu alistamento foi em em \033[1;31m{}.\033[m
            """.format(ano_hoje-ano,(ano_hoje-ano)-18,(ano + 18)))

    else:
        print("""
            Você tem {} anos em {}.
            Você tem que se alistar IMEDIATAMENTE!
            """.format(ano_hoje-ano,ano_hoje))
elif sexo == 2:
    print("\033[1;32m-*\033[m"*20)
    print("Você é do sexo FEMININO" \
    "\nO seu alistamento NÃO É OBRIGATÓRIO!")
    print("\033[1;32m-*\033[m"*20)

else:
    print("Não válido.")