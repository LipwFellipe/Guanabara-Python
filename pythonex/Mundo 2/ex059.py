escolha = 1
while escolha != 5:
    print(f'{"\033[36m{Selecione Dois valores}\033[m":=^50}')
    valor1 = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))
    escolha = int(input("""\033[31m[1]somar
\033[32m[2]multiplicar
\033[33m[3]maior
\033[34m[4]novos números
\033[35m[5]sair do programa\033[m """))
    if escolha == 1:
        print(f"O resultado é \033[32m{valor1+valor2}\033[m")
    if escolha == 2:
        print(f"O resultado é \033[32m{valor1*valor2}\033[m")
    if escolha == 3:
        if valor1 > valor2:
            maior = valor1
            print(f"O numero maior é \033[32m{maior}\033[m")
        else:
            maior = valor2
            print(f"O numero maior é \033[32m{maior}\033[m")
    if escolha == 4:
        escolha -= 1
    if escolha > 5:
        print("Valor inválido... \n\033[31mTente novamente\033[m")
print(f'{"\033[36m{Finalizado}\033[m":=^50}')
