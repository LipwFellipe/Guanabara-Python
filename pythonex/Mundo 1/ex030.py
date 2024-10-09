# Reconhecendoum numero PAR ou IMPAR
p = int(input('Digite um numero que irei dizer se é IMPAR ou PAR: '))
r = p % 2
if r == 0:
    print(f'Teu numero é \033[35mpar\033[m! (\033[35m{p}\033[m)')
if r == 1:
    print(f'Teu numero é \033[36mimpar\033[m! (\033[36m{p}\033[m)')
