n = int(input("Digite um numero:"))
res = str(input("Quer continuar? [S/N]")).upper()
s = 0 + n
c = 1
ma, me = n, n
while res == "S":
    n = int(input("Digite um numero:"))
    me = n if me > n else me + 0
    ma = n if ma < n else ma + 0
    c += 1
    s += n
    res = str(input("Quer continuar? [S/N]")).upper()
print(f"Voce digitou {c} numeros e a média foi de {s / c} \nO maior numero foi {ma} e o menor foi {me}")
