s1 = float(input('O \033[36mprimeiro segmento\033[m equivale a: '))
s2 = float(input('O \033[34msegundo segmento\033[m equivale a: '))
s3 = float(input('O \033[35mterceiro segmento\033[m equivale a: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Pode se formar um \033[33mtriagulo ', end='')
    if s1 == s2 and s2 == s3:
        print('EQUILÁTERO\033[m')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO\033[m')
    else:
        print('ISÓSCELES\033[m')
else:
    print('\033[31mNÃO\033[m pode se formar um triangulo!')
#FIZ UM CODE GIGANTE PARA O PROF FAZER ISSO EM 13 LINHAS