pt = int(input("Digite o primeiro termo de uma PA:"))
r = int(input("Digite a Razão dessa PA:"))
dez = pt + r * 10
c = 0
for dez in range(pt, dez, r):
    print(dez, end=" → ")
print("Acabou")
while c < 10:
    print(pt, end=" → ")
    c += 1
    pt += r
print("Acabou de novo☺")
