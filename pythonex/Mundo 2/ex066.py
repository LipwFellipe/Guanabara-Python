s = 0
while True:
    n = int(input("Digite um numero [999 para cancelar]: "))
    if n == 999:
        break
    s += n
print(f"A soma dos numeros são {s}")