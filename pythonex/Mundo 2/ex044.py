print(f'{"\033[35m{Loja do Lipw}\033[m":=^38}')
c = float(input('\033[36mQual foi o valor gasto?\033[m '))
escolha = int(input('''\033[36mSelecione o metodo de pagamento\033[m:
\033[34m[1]\033[m Pagar a vista
\033[33m[2]\033[m Á vista no cartão
\033[32m[3]\033[m Em até 2x no cartão
\033[31m[4]\033[m 3x ou mais no cartão 
\033[35m Qual opção? \033[m'''))
if escolha == 1:
    print(f'O valor a ser pago irá ser de \033[32m{(c * 10 / 100 - c) * -1:.2f}\033[m pois recebe 10% de desconto')
elif escolha == 2:
    print(f'O valor será de \033[32m{(c * 5 / 100 - c) * -1:.2f}\033[m pois recebe um desconto de 5%')
elif escolha == 3:
    print(f'O valor será de \033[32m{c/2:.2f}\033[m na primeira e consecutiva parcela \nPois não possui juros nem desconto')
elif escolha == 4:
    c1 = int(input(f'\033[36mQuantas vezes gostaria de parcelar?\033[m '))
    conta = (c * 20 / 100 + c)
    print(f'Sua compra de \033[32m{c:.2f}\033[m foi para \033[32m{conta:.2f}\033[m.')
    print(f'O valor em cada parcela será de \033[32m{conta / c1:.2f}\033[m pois possui juros de \033[34m20%\033[m')
