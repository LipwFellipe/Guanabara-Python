import random
vit = 0
while True:
    ej = int(input("Digite um numero de 1 a 10: "))
    PI = str(input("Par ou impar? [P]/[I]")).upper()
    ec = random.randint(0, 10)
    soma = ej + ec
    print(soma)
    if PI == "I" and soma % 2 == 0:
        print(f"Voce perdeu pois a soma de {ej} e {ec} é igual a {soma} deu PAR")
        break
    elif PI == "I" and soma % 2 != 0:
        print(f"Boaaaaaaaaaa, o computador colocou {ec} que a soma {soma} fica IMPAR")
        vit += 1
    elif PI == "P" and soma % 2 == 0:
        print(f"Boaaaaaaaaaa, o computador colocou {ec} que a soma {soma} fica PAR")
        vit += 1
    if PI == "P" and soma % 2 != 0:
        print(f"Voce perdeu pois a soma de {ej} e {ec} é igual a {soma} deu PAR")
        break
print(f"Voce teve um total de {vit} vitorias")
