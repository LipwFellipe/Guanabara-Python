"""Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores"""

cm = 0
cn = 0
for c in range(1, 8):
    p = int(input(f"\033[35mDigite o ano que a {c}ª pessoa nasceu: "))
    if 2024 - p >= 18:
        print("\033[34mUAU, ELE JÁ É MAIOR DE IDADE\033[m")
        cm += 1
    else:
        print("\033[31mELE NÃO É MAIOR DE IDADE\033[m")
        cn += 1
print(f"""O numero de pessoas maiores de idade é \033[34m{cm}\033[m
O numero de pessoas menores de idade é \033[31m{cn}\033[m""")