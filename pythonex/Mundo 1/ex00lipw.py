# Estou tentando melhorar em porcentagem, ent lá vai:
R1=float(input('A primeira nota do aluno: '))
R2=float(input('A segunda nota do aluno: '))
print(f'A média desse aluno é {(R1+R2)/2}')

s=int(input('Qual seu salario? '))
print(f'O salario do nego antes era {s} e agr com os 15% é {s+(s*15)/100}')

p = float(input('Quantos reais é aquela bolsa para a Raquelzinha? '))
print(f'Já q aquela bolsa é {p:.2f},com o desconto de 15%, ela fica apenas {p-p*15/100:.2f}')

p1=float(input('Jorge, qual é o seu antigo salario?'))
print(f'já q seu salario de {p1:.2f}, teve um aumento de 15%, vc ganha {p1+p1*15/100:.2f} agr né?')

l = int(input('Quantas medalhas Lipw tem? '))
p = int(input('Quantas medalhas Pedro tem? '))
c = int(input('Quantas medalhas Cavim tem? '))
if l > p > c:
    print('Em primeiro lugar ficará Lipw\nEm segundo lugar ficará Pedro\nEm terceiro ficará Cavim')
if l > p < c:
    print('Em primeiro lugar ficará Lipw\nEm segundo lugar ficará Cavim\nEm terceiro ficará Pedro')
if p > l > c:
    print('Em primeiro lugar ficará Pedro\nEm segundo lugar ficará Lipw\nEm terceiro ficará Cavim')
if p > l < c:
    print('Em primeiro lugar ficará Pedro\nEm segundo lugar ficará Cavim\nEm terceiro ficará Pedro')
if c > p > l:
    print('Em primeiro lugar ficará Cavim\nEm segundo lugar ficará Pedro\nEm terceiro ficará Lipw')
if c > l > p:
        print('Em primeiro lugar ficará Cavim\nEm segundo lugar ficará Lipw\n Em terceiro ficará Pedro')
if l == p:
    print(f'Cavim tem {c} medalhas\nE Pedro e Lipw  estão com o mesmo tanto de medalhas({l})')
if l == c:
    print(f'Pedro tem {p} medalhas\nE Cavim e Lipw  estão com o mesmo tanto de medalhas({l})')
if p == c:
    print(f'Lipw tem {l} medalhas\nE Cavim e Lipw  estão com o mesmo tanto de medalhas({l})')
import random

def jogar():
    print("Bem-vindo ao Pedra, Papel ou Tesoura!")

    escolhas_possiveis = ["pedra", "papel", "tesoura"]

    while True:
        # Usuário faz uma escolha
        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o jogo): ").lower()

        if escolha_usuario == 'sair':
            print("Obrigado por jogar. Até mais!")
            break

        if escolha_usuario not in escolhas_possiveis:
            print("Escolha inválida. Tente novamente.")
            continue

        # Computador faz uma escolha aleatória
        escolha_computador = random.choice(escolhas_possiveis)

        print(f"Você escolheu {escolha_usuario}. O computador escolheu {escolha_computador}.")

        # Determina o vencedor
        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif (
            (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
            (escolha_usuario == "papel" and escolha_computador == "pedra") or
            (escolha_usuario == "tesoura" and escolha_computador == "papel")
        ):
            print("Você venceu!")
        else:
            print("Você perdeu!")

if __name__ == "__main__":
    jogar()

