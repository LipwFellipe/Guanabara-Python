# Analizador de numeros
algo = input('Digite algo: ')
if algo.isnumeric():
    print(f'É do tipo: \033[35m{"<class 'int'>"} \033[m')
else:
    print(f'É do tipo:\033[34m{type(algo)} \033[m')
if algo.isalpha():
    print(f'É alfabetico?\033[32m {algo.isalpha()} \033[m')
else:
    print(f'É alfabetico?\033[31m False \033[m')
if algo.isalnum():
    print(f'É alfanumerico?\033[32m {algo.isalnum()}\033[m ')
else:
    print(f'É alfanumerico?\033[31m False \033[m')
if algo.isnumeric():
    print(f'É numerico?\033[32m {algo.isnumeric()} \033[m ')
else:
    print(f'É numerico?\033[31m False \033[m')
if algo.isspace():
    print(f'Só tem espaço? \033[32m{algo.isspace()}\033[m ')
else:
    print(f'Só tem espaço?\033[31m False \033[m')
