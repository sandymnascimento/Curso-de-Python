frase = str(input('Digite uma frase: ')).upper()
print('A letra "A" aparece', frase.count('A'), 'vezes na frase.')
print(f'A primeira ocorrência da letra A é na posição {frase.find("A") + 1}.')
print(f'A última ocorrência da letra A é na posição {frase.rfind("A") + 1}.')
