# Desafio 24 Tem Santo apenas no começo;
c = input('Qual é a sua cidade? ')
c1 = c.title()
c2 = (c1.find('Santo', 0, 6))
if c2 == -1:
    print('Sua cidade não tem \033[34mSanto\033[m no inicio!')
if c2 == 0:
    print('Sua cidade tem \033[34mSanto\033[m no inicio!')
# Desafio 25 Tem silva em QUALQUER LUGAR;
n = input('Qual é o seu nome completo? ')
n1 = n.title()
print('Silva' in n1)
# Desafio extra que eu me propus
p = input('Digite seu nome: ').title()
j = (p.strip())
if 'Santos' in p:
    print(f'Seu nome tem \033[34mSantos\033[m na posição {j.find('Santos')+1}')
else:
    print('Seu nome \033[31mNÃO\033[m tem \033[34mSantos\033[m')
