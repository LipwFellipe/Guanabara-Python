#Calcular o angulo em tangente, cosseno e seno FAIL
import math

a = int(input('Digite o angulo para calcular: '))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print(f'Cosseno é {c:.2f}\nSeno é {s:.2f} \nTangente é {t:.2f}')