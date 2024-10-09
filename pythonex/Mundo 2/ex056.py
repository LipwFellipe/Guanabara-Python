# Programa que mostre a media da idade do grupo, quantas mulheres tem menos de 20 anos e quem é o homem mais velho
iveio = 0
veio = "str"
somaidd = 0
somaf = 0
for c in range(1, 5):
    print("--------DADOS PESSOAIS--------")
    n = str(input(f"Qual o nome da {c}ª pessoa? ")).title().strip()
    idd = int(input(f"qual a idade da {c}ª pessoa? "))
    somaidd += idd
    secso = str(input("Qual é o sexo dela? [M / F]")).upper().strip()
    if secso == "M" and idd > iveio:
        iveio = idd
        veio = n
    if secso == "F" and idd < 20:
        somaf += 1
media = somaidd / 4
print(f"""\033[35mA média da idade do grupo é \033[m{media}
\033[34mO nome do homem mais velho é \033[m{veio} \033[34me possui \033[m{iveio}
\033[33mNesses dados existem \033[m{somaf} mulheres que são menores de 20 anos""")
