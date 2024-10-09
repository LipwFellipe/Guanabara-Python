# Calcular o IMC de cada pessoa
p = float(input('Quantos kg vc está pesando nesse momento? '))
a = float(input('Qual a sua altura? '))
imc = ((p / a) / a)
print(f'O \033[36mIMC\033[m dessa pessoa é \033[36m{imc:.2f}\033[m')
if imc < 18.5:
    print('\033[34mSeu peso está abaixo do peso\033[m \n magrelão, Julia reiskkk')
elif imc >= 18.5 and imc <= 24.9:
    print('\033[32mPeso adequado\033[m \033[34m PARABÉNS PELO CORPO SENSACIONAL')
elif imc >= 25 and imc <= 29.9:
    print('\033[36mSobrepeso\033[m, Maneire um pouco na comida!')
elif imc > 30.0:
    print('\033[35mObesidades\033[m, \033[31mSE TRATE POR FAVOR\033[m')
