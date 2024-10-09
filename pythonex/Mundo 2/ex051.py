"""Ex51"""

pt = int(input("Digite o primeiro termo de uma PA:"))
r = int(input("Digite a Razão dessa PA:"))
d = pt + (10 - 1) * r
for c in range(pt, d+r, r):
    print(c, end=" → ")
print("ACABOU☻")