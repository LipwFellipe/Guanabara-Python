# PEDRA PAPEL OU TESOURA? ESCOLHA
import random

print('\033[35mPedra\033[m, \033[33mPapel\033[m ou \033[34mTesoura \033[32m[THE GAME]\033[m')
ej = input('''Qual a sua escolha?
[1] \033[35mPedra\033[m
[2] \033[33mPapel\033[m
[3] \033[34mTesoura\033[m
\033[36mQual sua escolha?\033[m ''')
mylist = ['Tesoura', 'Papel', 'Pedra']
ec = random.choice(mylist)
# GANHOS
if ej == '3' and ec == 'Papel':
    print(f'O computador jogou \033[33m{ec}\033[m\n Logo você \033[32mGANHOU PARABÉNS\033[m')
elif ej == '2' and ec == 'Pedra':
    print(f'O computador jogou \033[33m{ec}\033[m\n Logo você \033[32mGANHOU PARABÉNS\033[m')
elif ej == '1' and ec == 'Tesoura':
    print(f'O computador jogou \033[33m{ec}\033[m\n Logo você \033[32mGANHOU PARABÉNS\033[m')
# LOSES
if ej == '3' and ec == 'Pedra':
    print(f'O computador jogou \033[33m{ec}\033[m\n Logo você \033[31mPERDEU, QUE TRISTE\033[m')
elif ej == '2' and ec == 'Tesoura':
    print(f'O computador jogou \033[33m{ec}\033[m\n Logo você \033[31mPERDEU, QUE TRISTE\033[m')
elif ej == '1' and ec == 'Papel':
    print(f'O computador jogou \033[33m{ec}\033[m\n Logo você \033[31mPERDEU, QUE TRISTE\033[m')
# EMPATES
if ej == '3' and ec == 'Tesoura':
    print(f'O computador jogou \033[34m{ec}\033[m\n E o jogo \033[33mEMPATOU\033[m')
elif ej == '2' and ec == 'Papel':
    print(f'O computador jogou \033[34m{ec}\033[m\n E o jogo \033[33mEMPATOU\033[m')
elif ej == '1' and ec == 'Pedra':
    print(f'O computador jogou \033[34m{ec}\033[m\n E o jogo \033[33mEMPATOU\033[m')
