import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é igual a {raiz}')
print(f'aredondar para cima, fica: {math.ceil(raiz)}')
print(f'aredondar para baixo, fica: {math.floor(raiz)}')
