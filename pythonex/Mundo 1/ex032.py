from datetime import date
a = int(input('Digite o Ano que deseja saber se é \033[35mBissexto\033[m ou não: \033[34m(COLOQUE O PARA COLOCAR O ANO DA MAQUINA) \033[m'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} \033[32mé\033[m \033[35mbissexto\033[m!')
else:
    print(f'O ano {a} \033[31mNÃO\033[m é \033[35mbissexto\033[m!')
