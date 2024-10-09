# O prof escolheu um aluno aleatorio de 4 :) FAIL
import random

a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo? '))
a3 = str(input('Qual o nome do terceiro? '))
a4 = str(input('Qual o nome do quarto? '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f"Dentre vcs {a1}, {a2}, {a3}, {a4}. \nEu escolho vc {escolhido}")
