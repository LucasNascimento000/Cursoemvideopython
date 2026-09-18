frase = str(input('Digite uma frase: ')).strip().lower()

print(f'A letra A aparece {frase.count('a')} vezes nas frase. \n'
      f'A primeira letra A apareceu na posiçao {frase.find('a') + 1}. \n'
      f'A última letra A apareceu na posiçao {frase.rfind('a') + 1}')
