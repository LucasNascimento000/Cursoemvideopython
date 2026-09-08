sal = float(input('Qual o salário do colaborador? R$'))
ajuste = sal + (sal * 15 / 100)

print(f'O salário antigo de R${sal:.2f} teve um reajuste de 15%, ficando no valor de R${ajuste:.2f}')
