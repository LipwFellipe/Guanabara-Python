n = int(input('Digite um numero para converter: '))
escolha = input('''CONVERSOR DE NUMEROS:
[1] Transformar numero em \033[32mBINARIO\033[m
[2] Transformar numero em \033[35mOCTAL\033[m
[3] Transformar numero em \033[36mHEXADECIMAL\033[m  ''')
if escolha == '1':
    print(format(n, 'b'))
elif escolha == '2':
    print(format(n, 'o'))
elif escolha == '3':
    print(format(n, 'x'))