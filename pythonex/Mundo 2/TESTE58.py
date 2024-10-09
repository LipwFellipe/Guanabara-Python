import random
con = 0
j = 11
c = random.randint(0, 10)
print("Jogo de Advinhação")
while j != c:
    j = int(input(f"Qual numero entre 0 a 10 você acha que o computador escolheu? {c}"))
    con += 1
    if j == c:
        print("\nVocê acertou!!!")
    else:
        print("\nERRADO")
print(f"Você teve {con} tentativas!")
