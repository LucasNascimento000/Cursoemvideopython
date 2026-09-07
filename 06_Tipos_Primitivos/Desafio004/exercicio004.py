x = input('Digite um valor: ')

print(f'O tipo primitivo deste valor é {type(x)}')
print(f'Pode aparecer no terminal? {x.isprintable()}')
print(f'Só tem espacos? {x.isspace()}')
print(f'É um número? {x.isnumeric()}')
print(f'É alfabético? {x.isalpha()}')
print(f'É alfanúmerico? {x.isalnum()}')
print(f'Está em maiúsculas? {x.isupper()}')
print(f'Está em minúsculas? {x.islower()}')
print(f'Está capitalizada? {x.istitle()}')

