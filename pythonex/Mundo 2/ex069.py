print(f"{'CADASTRE UMA PESSOA':=^40}")
h = 0
mu20 = 0
idd18 = 0
while True:
    idd = int(input("Qual sua idade? "))
    if idd > 18:
        idd18 += 1
    Sexo = " "
    while Sexo not in "HF":
        Sexo = str(input("Qual é o secso da pessoa? [H/F]")).upper()
    if Sexo == "H":
        h += 1
    c = " "
    while c not in "SN":
        c = str(input("Quer continuar? [S/N]")).upper()
    if idd < 20 and Sexo == "F":
        mu20 += 1
    if c == "N":
        break
print(f"Ao total tiveram {idd18} pessoas com mais de 18 anos.")
print(f"Ao total tiveram {h} HOMENS")
print(f"Ao total tiveram {mu20} mulheres com menos de 20 anos")
