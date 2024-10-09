s = 0
for c in range(0, 501):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        s = s + c
verde = ("\033[32m", f"{s}")
co = "A soma dos números ímpares múltiplos de 3 até 500 é ".join(verde)
print(f"A soma dos números ímpares múltiplos de 3 até 500 é \033[32m{s}")
# Para juntar a cor com o somatório eu usei esse .join sem nenhum espaço
