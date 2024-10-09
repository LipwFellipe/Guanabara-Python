print(F"{'LOJA BARATEXXX':=^40}")
som = pbp = mil = contador = 0
pb = ""
while True:
    np = str(input("Nome do produto: "))
    p = float(input("Preço do produto: "))
    contador += 1
    if contador == 1:
        pbp = p
    if p >= 1000:
        mil += 1
    som += p
    if p < pbp:
        pbp = p
        pb = np
    c = str(input("Quer continuar? [S/N]")).upper()
    if c == 'N':
        break
print(f"O total da compra foi R${som:.2f}")
print(f"Temos {mil} produto custando mais de R$1000.00")
print(f"O produto mais barato foi {pb} custando R${pbp:.2f}")
