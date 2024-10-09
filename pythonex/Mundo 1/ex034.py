# Dependendo de quanto seja o salario de um pagão, recebra um aumento diferente
s = int(input('Quanto vc recebe de salário? '))
s10 = (s * 10) / 100 + s
s15 = (s * 15) / 100 + s
if s >= 1250.00:
    print(f'Seu salario terá um aumento de \033[36m10%\033[m e ficará \033[32mR${s10:.2f}\033[m')
if s <= 1249.00:
    print(f'Seu salario terá um aumento de \033[36m15%\033[m, Logo ficará \033[32mR${s15:.2f}\033[m')
# Outra forma q pensei em fazer
if s >= 1250.00:
    n1 = (s * 10) / 100 + s
else:
    n1 = (s * 15) / 100 + s
print(f'O seu novo salário de \033[32mR${s:.2f}\033[m vai para \033[32mR${n1:.2f}\033[m')
