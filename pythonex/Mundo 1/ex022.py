# Analizador de nomes
f = input('Digite seu nome: ')
c = f.split()
print('Seu nome em maiusculas é ', f.upper())
print('Seu nome em minusculas é ', f.lower())
print('Seu nome tem', len(''.join(c)), 'letras')
print('Seu nome tem', len(c[0]), 'letras na primeira palavra')
print('Seu nome tem', len(c[-1]), 'letras na ultima palavra')
