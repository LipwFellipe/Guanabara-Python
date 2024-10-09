# BEM VINDO AO CHEFE FINAL, Saporra é mais dificil q vc pensa
s1 = float(input('O \033[36mprimeiro segmento\033[m equivale a: '))
s2 = float(input('O \033[34msegundo segmento\033[m equivale a: '))
s3 = float(input('O \033[35mterceiro segmento\033[m equivale a: '))
# Descobrindo qual é maior segmento
maior = s1
if s2 > s1 and s2 > s3:
    maior = s2
if s3 > s1 and s3 > s2:
    maior = s3
# S1 Maior
if maior == s1 and s2 + s3 >= s1:
    print(f'A soma dos segmentos menores equivale a \033[33m{s2 + s3}\033[m\nE é possivel \033[32mformar um triangulo!\033[m')
if s2 + s3 < s1:
    print(f'A soma dos segmentos menores equivale a \033[33m{s2 + s3}\033[m\nE \033[31mNÃO\033[m é possivel formar um \033[33mtriangulo\033[m')
# S2 Maior
if maior == s2 and s1 + s3 >= s2:
    print(f'A soma dos segmentos menores equivale a \033[33m{s1 + s3}\033[m\nE é possivel \033[32mformar um triangulo\033[m')
if s1 + s3 < s2:
    print(f'A soma dos segmentos menores equivale a \033[33m{s1 + s3}\033[m\nE \033[31mNÃO\033[m é possivel formar um \033[33mtriangulo\033[m')
# S3 Maior
if maior == s3 and s2 + s1 >= s3:
    print(f'A soma dos segmentos menores equivale a \033[33m{s2 + s1}\033[m\nE é possivel \033[32mformar um triangulo\033[m')
if s2 + s1 < s3:
    print(f'A soma dos segmentos menores equivale a \033[33m{s2 + s1}\033[m\nE \033[31mNÃO\033[m é possivel formar um \033[33mtriangulo\033[m')
