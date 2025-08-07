# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
cidade = input("Digite o nome da cidade que você nasceu: ")

cidade = cidade.strip()

cidade_lst = cidade.split()

print(cidade_lst[0].lower() == "santo")
    


