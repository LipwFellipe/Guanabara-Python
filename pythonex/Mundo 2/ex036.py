# Menino financiando uma casa
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Quanto você recebe de salário? '))
anos = float(input('Em quantos anos você vai pagar essa casa? '))
messes = anos * 12
pm = (salario*30) / 100
v = (casa / messes)
if v <= -1:
    print(f'Você conseguiu pagar sua casa em {messes:.0f} messes e isso te custou um total de R${pm:.2f} em cada mês ')
elif v >= 0:
    print(f'Você não conseguirá financiar sua casa com 30% do seus R${salario:.2f} em todos os {messes:.0f} messes :(')
print(pm)