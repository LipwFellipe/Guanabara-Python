# HIPOTENUSAAAA
from math import sqrt

ca = float(input('Quanto é o cateto adjacente? '))
co = float(input('Quanto é o cateto oposto? '))
h = sqrt((ca ** 2)+(co ** 2))
print('O valor da hypotenuse é {:.2f}'.format(h))
#Outra forma de fazer sem usar o import
ca = float(input('Qual o valor do cateto adjacente? '))
co = float(input('Qual o valor do cateto oposto? '))
h = ((ca**2)+(co**2)) ** (1/2)
print(f'A hipotenusa é {h:.2f}')