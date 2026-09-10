from math import radians, sin, cos, tan

ang =float(input('Digite o ângulo que você deseja: '))

rad = radians(ang)

print(f'O ângulo de {ang} tem o SENO de {sin(rad):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(rad):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan(rad):.2f}')
