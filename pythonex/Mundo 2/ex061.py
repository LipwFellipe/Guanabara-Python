# TERMOS DE UMA PA COM O WHILE

n1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a Razão dessa PA: "))
c = 0
while c != 10:
    c += 1
    print(n1, end="")
    n1 += r
    print(" → " if c < 10 else " Acabou", end="")
