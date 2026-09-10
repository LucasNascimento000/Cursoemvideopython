import math

Co = float(input('Comprimento do cateto oposto: '))
Ca = float(input('comprimento do cateto adjacente: '))

hip = math.hypot(Co, Ca)

print('-'* 30)
print(f'O comprimento do cateto oposto é {Co} \n'
      f'O comprimento do cateto adjacente é {Ca} \n'
      f'E a hipotenusa é {hip:.2f}')
