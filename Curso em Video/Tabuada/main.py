try: 
    entrada = int(input("Digite um número inteiro: "))

    for i in range(10):
        tabuada = (i+1)*entrada
        print(f"{entrada} x {i+1} = {tabuada}")
except:
    print("Esse não é um numero inteiro!")