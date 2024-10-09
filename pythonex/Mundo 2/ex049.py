#Tabuada usando o for
t = int(input('\033[32mDiga um numero para fazer a tabuada:) '))
for c in range(0, 11):
    print(f"{t} * {c} =", t * c)
