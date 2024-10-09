pt = int(input("Digite o primeiro termo de uma PA:"))
r = int(input("Digite a Razão dessa PA:"))
ult = pt + r * 10
mt = 1

for ult in range(pt, ult, r):
    print(ult, end=" → ")
print("PAUSA")
while mt != 0:
    mt = int(input("Quantos termos a mais você quer mostrar?"))
    p = ult + r * mt
    for ult in range(ult, p, r):
        print(ult, end=" → ")
    print("PAUSA")
print("perai")
