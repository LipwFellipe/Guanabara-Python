"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos"""
menor = 0
maior = 0
for c in range(1, 6):
    num = float(input(f"Digite o numero da {c}ª pessoa: "))
    if c == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print(f"O maior peso foi de {maior} \n O menor peso foi de {menor}")
