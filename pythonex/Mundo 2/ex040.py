# Média de dois alunos usando if e elif
n1 = float(input('De 0 a 10 digite a sua primeira nota do Bimestre: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1 + n2) / 2
if s < 5:
    print(f'Você foi ... \n\033[31mREPROVADO\033[m\nPois tirou uma média de {s}\033[31m QUE HORROR DE NOTAAAA\033[31m')
elif s >= 7.0:
    print(f'Você foi .... \n\033[32mAPROVADO\033[m\nPois tirou uma média de {s} \033[35mPARABÉNS\033[m')
elif 5.0 <= s <= 6.9:
    print(f"VoCê está de \033[31mRECUPERAÇÃO\033[m, pois sua média é {s}")
