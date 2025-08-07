# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

média = (n1 + n2)/2

if média < 5.0:
    print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.\nO aluno está...".format(n1,n2,média))
    print("\n")
    print("=-*"*10)
    print("\033[1;31mREPROVADO\033[m")
    print("=-*"*10)
    print("\n")
elif média >=5.0 and média <7:
    print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.\nO aluno está...".format(n1,n2,média))
    print("\n")
    print("=-*"*10)
    print("\033[1;33mEM RECUPERAÇÃO\033[m")
    print("=-*"*10)
    print("\n")

elif média >= 7.0:
    print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.\nO aluno está...".format(n1,n2,média))
    print("\n")
    print("=-*"*10)
    print("\033[1;32mAPROVADO!\033[m")
    print("=-*"*10)
    print("\n")