# Carro pego no radar!!!
import os as sistema
v = float(input('Qual era a velocidade do seu carro no momento do radar? '))
multa = (v-80)*7.00
if v > 80:
    print(f'''\033[31mSeu carro foi multado!
A multa é {multa:.2f}R$\033[m''')
else:
    print(f'\033[34mTenha um bom dia Senhor.{sistema.getlogin()}!\033[m')
