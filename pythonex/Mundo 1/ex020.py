# Um professor quer q forme uma ordem aleatoria de 4 alunos
import random
a1 = str(input('Nomeie um aluno: '))
a2 = str(input('Nomeie outro aluno: '))
a3 = str(input('Nomeie outro aluno: '))
a4 = str(input('Nomeie outro aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'{lista}')
