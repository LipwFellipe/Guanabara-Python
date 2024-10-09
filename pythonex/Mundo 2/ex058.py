import random
nc = random.randint(0, 10)
c = 1
print("Olá, escolhi um numero aleatorio de 0 a 10, consegue advinhar que numero é esse?")
np = int(input("Resposta:"))
if np > nc:
    print("O numero é menor...")
if np < nc:
    print("O numero é maior...")
while np != nc:
    np = int(input("Tente novamente... "))
    c += 1
    if np > nc:
        print("O numero é menor...")
    elif np < nc:
        print("O numero é maior...")
print(f"Vc acertou!! \nVc teve {c} tentativas para acertar o numero.")
