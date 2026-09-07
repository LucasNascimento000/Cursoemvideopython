largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

print(f'Sua parede tem a dimensao de {largura}x{altura} e sua área é de {area:.1f}m²')
print(f'Para pintar essa parede, você precisará de {area / 2}L de tinta.')
