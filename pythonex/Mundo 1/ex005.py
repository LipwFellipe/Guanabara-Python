# Calculos de Porcentagem (Aumento de Salario)

salario = float(input('\033[36mQuanto é o salario que você recebe? '))
print(f'O seu salario de {salario:.2f}, com o 15% de aumento vai para {salario+(salario*15/100):.2f}.\033[m')

# Calculos de Porcentagem (Desconto da camisa)
camisa = float(input('\033[30mA camisa que vc gostou custa quantos reais? '))
print(f'Já q ela é {camisa:.2f}, com o novo desconto'
      f' de 5% que estou te oferecendo, ela se torna {camisa-(camisa*20)/100}')

# Quantas latas de tinta um senhor vai necessitar para pintar uma parede

print('\033[36mSenhor Agnaldo está em duvida de quantas latas de tinta\nEle vai precisar para poder pintar uma parede')
L = float(input('\033[34mQuantos metros de largura a parede que o Senhor Agnaldo vai pintar tem? '))
A = float(input('\033[35mQuantos metros tem de altura? '))
print(f'\033[36mPara se pintar essa parede inteira será necessario {(L*A)/2} latas de tinta')

# Conversor de real para dolar

real = float(input('\033[32mVc tem quantos reais na sua carteira? R$'))
quad = real/4.96
print(f'Vc tem R${real:.2f} reais, com isso é possivel comprar U${quad:.2f} dolares')

# Tabuada
t = int(input('\033[33mDiga um numero para fazer a tabuada:) '))
print('\n', t, f'* 1 = {t*1} \n', t, f'* 2 = {t*2} \n', t, f'* 3 = {t*3} \n'
                                                           f'', t, f'* 4 = {t*4} \n', t, f'* 5 = {t*5} \n', t,
      f'* 6 = {t * 6}'f' \n', t, f'* 7 = {t*7} \n', t, f'* 8 = {t*8} \n', t, f'* 9 = {t*9} \n', t, f'* 10 = {t*10}')

# Conversor de metros

m = int(input('\033[32mDigita um valor em metros ai: '))
print(f'{m} metros equivalem à {m*100} centimetros \n e equivalem à {m*1000} milimetros ')

# Analizador de numeros

n = int(input('\033[mDigita um numero ai pô '))
print('O numero escolhido é', n, f'\n o sucessor do seu numero é {n + 1} \n e o antecessor é {n - 1} '
                                 f'\n o seu triplo é {n*3} \n o seu dobro é {n*2} \n e a raiz quadrada é {n**(1/2)}')

# Média de Notas do Lipw
print('\033[32mVocê irá calcular a média de um aluno em sua faculdade.')
r1 = (float(input('Digite a primeira nota do Lipw: ')))
r2 = float(input('Digite a segunda nota do Lipw:'))
print(f'A média de Lipw gostoso é igual a {(r1+r2)/2}')
