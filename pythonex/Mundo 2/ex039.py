ano = int(input('Olá \033[31mJ\033[32mo\033[33mv\033[34me\033[35mm\033[m, Informe sua data de nascimento aqui: '))
idd = (ano - 2023) * (-1)
if idd == 18:
    print('Você deve fazer o \033[34mAlistamento obrigátorio\033[m neste \033[31mANO\033[m ainda')
elif idd > 18:
    print(f'Seu alistamento já venceu tem \033[36m{idd - 18} anos\033[m')
else:
    print(f'Ainda faltam \033[32m{(idd - 18) * -1} anos\033[m para vc se alistar!')
