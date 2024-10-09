c = 0
termo = 10
cont = 10
n1 = int(input("Digite o primeiro termo da PA: "))
ra = int(input("Digite a Razão da PA: "))
while termo != 0:
    while c < termo:
        n1 += ra
        c += 1
        print(n1-ra, end="")
        print(" x " if c < 10 else " PAUSA ", end="")
    termo = int(input("\nDeseja adicionar mais quantos termos?"))
    cont += termo
    c -= termo
print(f"O total de termos que a razão teve é {cont}")
