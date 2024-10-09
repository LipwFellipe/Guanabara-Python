from random import randint
s1 = randint(0, 9)
s2 = randint(0, 9)
s3 = randint(0, 9)
s4 = randint(0, 9)
l1 = (str(s1))
l2 = (str(s2))
l3 = (str(s3))
l4 = (str(s4))
# UAU, COMO POSSO SER TÃO BURRO
print(f'''O seu numero gerado randomicamente é {l1+l2+l3+l4}, porém
A \033[32mUnidade\033[m é {s4}
A \033[33mDezena\033[m é {s3}
A \033[34mCentena\033[m é {s2}
A \033[35mMilhar\033[m é {s1}''')
# Não tô enferrujado
n = input('Digite um numero qualquer: ')
print(f'A \033[32mMilhar\033[m é {n[0]}\033[m')
print(f'A \033[33mCentena\033[m é \033[33m{n[1]}\033[m')
print(f'A \033[34mDezena\033[m é \033[34m{n[2]}\033[m')
print(f'A \033[35mUnidade\033[m é \033[35m{n[3]}\033[m')
