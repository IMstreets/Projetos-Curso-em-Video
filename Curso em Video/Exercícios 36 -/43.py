peso = float(input("Digite o peso:(Kg) "))
alt = float(input("Digite a altura:(m) "))

imc = peso/(alt**2)

if imc < 18.5:
    print("Seu IMC é \033[1;31m{:.1f}\033[m e você está \033[1;31mABAIXO DO PESO\033[m".format(imc))

elif 18.5 <= imc < 25:
    print("Seu IMC é \033[1;32m{:.1f}\033[m e você está com o \033[1;32mPESO IDEAL!\033[m".format(imc))

elif 25 <= imc < 30:
    print("Seu IMC é \033[1;33m{:.1f}\033[m e você está com o \033[1;33mSOBREPESO!\033[m".format(imc))

elif 30 <= imc < 40:
    print("Seu IMC é \033[1;31m{:.1f}\033[m e você está com o \033[1;31mOBESIDADE!\033[m".format(imc))

elif 40 <= imc > 40:
    print("Seu IMC é \033[1;31m{:.1f}\033[m e você está com o \033[1;31mOBESIDADE MÓRBIDA!\033[m".format(imc))

