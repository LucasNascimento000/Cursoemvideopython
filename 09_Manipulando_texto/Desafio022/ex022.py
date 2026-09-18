nome = input('Digite seu nome completo: ').strip()
Qlnome = (len(nome)) - (nome.count(" "))

print(f"""
O seu nome maiúsculo é {nome.upper()}
O seu nome minúsculo é {nome.lower()}
Ele possui {Qlnome} letras 
O primeiro nome é {nome.split()[0].title()} e possui {len(nome.split()[0])} letras
""")

print(Qlnome)