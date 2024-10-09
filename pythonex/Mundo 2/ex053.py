"""Crie um programa que leia uma frase qualquer e diga se é um palíndromo"""

f = str(input("Digite uma Frase: ")).upper().strip()
s = f.split()
d = "".join(s)
r = d[::-1]
print(f"Sua frase é {d} e ela reversa é", d[::-1])
if d == r:
    print("Sua frase é um palíndromo")
else:
    print("Sua frase NÃO é um palíndromo")
