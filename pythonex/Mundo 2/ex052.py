"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

n = int(input("Coloque o numero: "))
t = 0
for c in range(1, n+1):
    if (n > 1) and (n % c == 0):
        print('\033[32m', c, '\033[m', end=" ")
        t+=1
    else:
        print('\033[31m', c,'\033[m', end=" ")
if t == 2:
    print("\nSeu numero é primo, pois foi dividido", t, "vezes")
else:
    print("\nNão é primo, pois foi dividido", t, "vezes.")
