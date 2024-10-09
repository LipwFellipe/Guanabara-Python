n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
esc = 4
while esc != 5:
    print("""\033[31m[1]Somar
\033[32m[2]Multiplicar
\033[33m[3]Maior
\033[34m[4]Novos números
\033[35m[5]Sair do programa\033[m """)
    esc = int(input("Digite o valor correspondente: "))
    if esc == 1: print(f"{n1}+{n2}={n1 + n2}")
    if esc == 2: print(f"{n1}*{n2}={n1*n2}")
    if esc == 3:
        if n1 > n2:
            print(f"Dentre {n1} e {n2}, O maior valor é {n1}")
        else:
            print(f"Dentre {n1} e {n2}, O maior valor é {n2}")
    if esc == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
print("Terminado.")

