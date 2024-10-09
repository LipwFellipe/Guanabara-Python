# Conversor MUNDIAL de temperaturas
t = float(input('Digite a temperatura: '))
R = input('Qual temperatura gostaria de calcular? (C / K / F ) ')
if R == 'C' or R == 'c':
    print(
        f'A temperatura em \033[32mCelcius\033[m colocada é \033[32m{t}\033[m\n para \033[31mFahrenheit\033[m é \033[31m{t * 1.8 + 32:.2f}\033[m\n para \033[34mKelvin\033[m é \033[34m{t + 273.15:.2f}\033[m')
elif R == 'K' or R == 'k':
    print(
        f'A temperatura em \033[34mKelvin\033[m colocada é \033[34m{t}\033[m \n para \033[31mFahrenheit\033[m é \033[31m{t * 1.8 - 459.67:.2f}\033[m \n para \033[32mCelcius\033[m é \033[32m{t - 273.15:.2f}\033[m')
elif R == 'F' or R == 'f':
    print(
        f'A temperatura em \033[31mFahrenheit\033[m colocada é \033[31m {t} \033[m \n para \033[32mCelcius\033[m é \033[32m{(t - 32) * 0.5555555:.2f}\033[m \n para \033[34mKelvin\033[m é \033[34m{(t - 32) * 0.5555555 + 273.15:.2f}\033[m')
