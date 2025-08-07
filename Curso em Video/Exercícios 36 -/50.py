# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("="*40)
print("10 PRIMEIROS DIGITOS DA PA")
print("="*40)
primeiro = int(input("Digite o primeiro termo dessa PA: "))
razão = int(input("Digite a razão dessa PA: "))
pa = primeiro
for i in range(1,11):
    print((pa),end=" -> ")
    pa += razão
print("Acabou")