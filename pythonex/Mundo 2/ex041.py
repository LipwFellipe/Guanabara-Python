ano = int(input('Digite seu ano de nascimento: '))
vrf = (ano - 2024) * -1
print(vrf)
if vrf >= 21:
    print(f'Com a sua idade {vrf} você só pode ser \033[35mMaster\033[m')
elif vrf == 20:
    print(f'Com a sua idade {vrf} você só pode ser \033[34mSênior\033[m')
elif 15 <= vrf <= 19:
    print(f'Com a sua idade {vrf} você só pode ser \033[33mJunior\033[m')
elif 10 <= vrf <= 14:
    print(f'Com a sua idade {vrf} você só pode ser \033[36mInfantil\033[m')
elif 9 <= vrf:
    print(f'Com a sua idade {vrf} você só pode ser \033[32mMirim\033[m')
