# TRANSFORMAR UM NUMERO REAL EM INTEIRO
from math import trunc
print('\033[31m Digite um numero REAL Ex:0.00\033[m')
r = float(input('Digite um \033[34mNumero Real\033[m que não seja \033[35mInteiro\033[m: '))
print(f'Seu \033[34mnumero real\033[m é \033[34m{r}\033[m e ele em \033[35mforma inteira\033[m é \033[35m{trunc(r)}\033[m ')

'''while True:
    try:
        nota = int(input("Informe a nota entre 0 e 10: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

print(nota)'''
