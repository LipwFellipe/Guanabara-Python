ter = int(input("Quantos termos quer mostrar?"))
a, b = 0, 1
c = 3
print(a, "→", b, end=" → ")
while c <= ter:
    t3 = a + b
    print(t3, end=" → ")
    a = b
    b = t3
    c += 1
print("Acabou")
