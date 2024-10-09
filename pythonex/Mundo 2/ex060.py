# Fazer ultilizando for e while
# Fatorial

num = int(input("Diga um numero para calcular o seu fatorial: "))
con = num
mult = 1
while con > 0:
    print(f"{con}", end="")
    print(" x " if con > 1 else " = ", end="")
    mult *= con
    con -= 1
print(f"{mult}")

"""n = int(input("Diga um numero pra fazer fatorial: "))
mu = 1
for c in range(n, 0, -1):
    print(c, end="")
    print(" x " if c > 1 else " = ", end="")
    mu *= c
    c -= 1
print(f"{mu}")"""