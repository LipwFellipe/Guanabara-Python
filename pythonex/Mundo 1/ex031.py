# Não faço nem ideia de q exercicio seja esse :p
k = float(input('Qual a distancia em km da viagem q tu foi? '))
if k <= 200:
    print(f'Sua viagem ficou \033[32mR${k*0.50:.2f}\033[m, pois cobrei 0.50 reais por km')
else:
    print(f'Sua viagem ficou em \033[32mR${k*0.45:.2f}\033[m, pois cobrei 0.45 reais por km')
# Ex com as variaveis igual do video pq achei interessante
if k <= 200:
    preco = (k*0.50)
else:
    preco = (k*0.45)
print(f'Tu me deve \033[32mR${preco:.2f}\033[m')
