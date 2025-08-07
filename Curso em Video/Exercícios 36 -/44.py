#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros


def menu():
    
    print("""
    Digite qual a forma de pagamento:
        \033[1;32m[ 1 ]\033[m À vista (PIX / DINHEIRO) 
        \033[1;32m[ 2 ]\033[m Crédito à vista
        \033[1;32m[ 3 ]\033[m Crédito 2x
        \033[1;32m[ 4 ]\033[m Crédito 3x ou mais
        """)

    opcao = int(input("Digite a sua opção: "))
    return opcao

while True:
    print("{:=^40}".format(" STREETSTORE "))
    valor = float(input("Digite o valor a ser pago: R$"))
    opcao = menu()
    if opcao == 1:
        desconto = 0.1 * valor
        valor *= 0.9
        print("O valor a ser pago é \033[1;33mR${:.2f}\033[m e você recebeu \033[1;32m10% de desconto no valor de R${:.2f}\033[m!".format(valor,desconto))
        break

    elif opcao == 2:
        desconto = 0.05 * valor
        valor *= 0.95
        
        print("O valor a ser pago é \033[1;33mR${:.2f}\033[m e você recebeu \033[1;32m5% de desconto no valor de R${:.2f}\033[m!".format(valor,desconto))
        break

    elif opcao == 3:
        print("O valor a ser pago é \033[1;33mR${:.2f}\033[m em \033[1;32m2x de R${:.2f} SEM JUROS\033[m!".format(valor,(valor/2)))
        break

    elif opcao == 4:
        opcao2 = int(input("Quantas parcelas serão? "))
        if opcao2 == 1 or opcao2 == 2:
            print("""Deseja voltar ao menu e selecionar outra opção para receber desconto? 
                \033[1;32m[ 1 ]\033[m Sim
                \033[1;32m[ 2 ]\033[m Não
                """)
            opcao3 = int(input("Digite sua opção: "))

            if opcao3 == 1:
                continue
            elif opcao3 == 2:
                valor *= 1.2
                print("O valor a ser pago é \033[1;33mR${:.2f}\033[m em \033[1;33m{} parcelas\033[m de \033[1;32mR${:.2f}\033[m.".format(valor,opcao2,(valor/opcao2)))
                break
            else:
                print("\033[1;31mOpção inválida, voltando ao menu!\033[m\n\n")
                continue
        else:
            valor *= 1.2
            print("O valor pago será \033[1;33mR${:.2f}\033[m em \033[1;33m{} parcelas\033[m de \033[1;33mR${:.2f} COM JUROS\033[m.".format(valor,opcao2,(valor/opcao2)))
            break
    else:
        print("\033[1;31mOpção inválida, voltando ao menu!\033[m\n\n")
        continue