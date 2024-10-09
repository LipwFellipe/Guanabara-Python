n = int(input("Digite um numero [999 para cancelar]: "))
v, s = 0, 0
while n != 999:
    v += 1
    s += n
    n = int(input("Digite um numero(999 para cancelar): "))
print(f"Voce digitou {v} numeros e a soma entre eles é {s}")
