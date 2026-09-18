num = int(input('Digite um número de 0 a 9999:  '))

milhar = num // 1000
centena = (num - milhar * 1000) // 100
dezena = (num - (milhar * 1000 + centena * 100)) // 10
unidade = (num - (milhar * 1000 + centena * 100 + dezena * 10))

print(f"""
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
""")
