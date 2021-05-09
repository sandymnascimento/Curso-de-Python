nome = input('Digite seu nome completo: ')
split = nome.split()

print('O seu nome é:', nome)
print('Em letras maiúsculas:', nome.upper())
print('Em letras minúsculas:', nome.lower())
print(f'O nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print('O primeiro nome tem', len(split[0]), 'letras.')  # find(' ') também retornaria o tam
