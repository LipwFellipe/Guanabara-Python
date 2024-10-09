# Carro Alugado
k = float(input('Quantos \033[32mkm\033[m tu andou? '))
d = int(input('Quantos \033[33mdias\033[m ele foi alugado? '))
print(f'Se ele ficou \033[33m{d} dias\033[m e andou \033[32m{k} kilometros\033[m, custará um total de \033[31mR${(60*d)+(k*0.15):.2f}')
