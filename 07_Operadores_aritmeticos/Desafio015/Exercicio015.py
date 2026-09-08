dia = float(input('Quantos dias o carro ficou alugado? '))
Km = float(input(f'Neste(s) {dia:.0f} dia(s), Quantos Km foram rodados? '))

valor_dia = dia * 60
valor_km = Km * 0.15



print()
print(f'Você utilizou o carro por {dia:.0f} dia(s), R$60 por dia fica R${valor_dia:.2f}')
print(f'E também rodou {Km}Km, R$0.15 por Km rodado fica R${valor_km:.2f}')
print()

print('Valor Dia(s)', f'R${valor_dia:>7.2f}')
print('Valor Km    ', f'R${valor_km:>7.2f}')
print('--------------------------')
print('Valor Final ', f'R${valor_dia + valor_km:>7.2f}')
