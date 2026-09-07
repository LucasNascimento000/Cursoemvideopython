distancia = float(input('Uma distancia em metros: '))

print(f'A medida de {distancia} corresponde a ')

print(f'{distancia / 1000}km \n'
      f'{distancia /100}hec \n'
      f'{distancia / 10}dam \n'
      f'{distancia * 10}dm \n'
      f'{distancia * 100}cm \n'
      f'{distancia * 1000}mm')
