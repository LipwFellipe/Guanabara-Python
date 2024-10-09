# Mostra quantos A tem na frase e suas respectivas posições
c = input('Digite seu nome: ').upper().strip()
c2 = ''.join(c)
if 'A' in c:
    print('\033[32mTem A no seu nome amigo ;)\033[m')
    print('Em seu nome tem', c.count('A'), 'vezes a letra A')
    print('Em seu nome a primeira letra A aparece na posição', c2.find('A') + 1)
    print('Em seu nome a ultima letra A aparece na posição', c2.rfind('A') + 1)
else:
    print('\033[31mNão tem A no seu nome amigo;(\033[m')

# Desafio 27, Mostrar apenas o primeiro nome e ultimo
l = c.title().split()
c4 = ' '.join(l)
print('Nome digitado:\033[33m', c4, '\033[m')
print('Primeiro nome:\033[33m', l[0], '\033[m')
print('Ultimo nome:\033[33m', l[-1], '\033[m')
