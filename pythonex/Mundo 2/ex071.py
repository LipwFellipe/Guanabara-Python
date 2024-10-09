print(f"{'CAIXA ELETRONICO':=^40}")
v = int(input("Digite um valor para sacar: R$"))
n50 = n20 = n10 = n1 = 0

while v >= 50:
    v -= 50
    n50 += 1
print(n50, "Notas de R$50,00")
while v >= 20:
    v -= 20
    n20 += 1
print(n20, "Notas de R$20,00")
while v >= 10:
    v -= 10
    n10 += 1
print(n10, "Notas de R$10,00")
while v >= 1:
    v -= 1
    n1 += 1
print(n1, "Notas de R$1,00")
