a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
# Menor
if a < b and a < c:
    print(f'O menor numero é {a}')
if b < a and b < c:
    print(f'O numero menor é {b}')
if c < a and c < b:
    print(f'O menor numero é {c}')
# Maior
if a > b and a > c:
    print(f'O maior numero é {a}')
if b > a and b > c:
    print(f'O numero maior é {b}')
if c > a and c > b:
    print(f'O maior numero é {c}')
