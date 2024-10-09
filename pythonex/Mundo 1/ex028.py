# Jogo de advinhações
import random
ec = random.randint(0, 5)
ep = int(input(f'''O computador escolheu um numero de 0 a 5 ({ec})
Tente acertar o numero chutando: '''))
if ep == ec:
    print('\033[32mVocê é FODA, acertou de primeira!\033[m')
else:
    print(f'\033[31mNoob, o numero era {ec} \033[m')
