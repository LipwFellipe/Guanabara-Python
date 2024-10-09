s = 0
print("\033[32mEu somarei todos os numeros pares e ignorarei os numeros impares que voce me falar\033[m")
for _ in range(0, 3):
    n = int(input("Digite um \033[35mnumero\033[m:"))
    if n % 2 == 0:
        s += n
        print("Somarei este numero")
    else:
        print("saporra é impar, ent eu não vou somar")
print(f"A somátoria dos numeros pares deu {s}")
