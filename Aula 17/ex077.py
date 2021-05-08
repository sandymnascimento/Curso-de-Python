palavras = (
'PROGRAMAR', 'PYTHON', 'LINGUAGEM', 'DESENVOLVIMENTO', 'TECNOLOGIA', 'ESTUDOS', 'APRENDER', 'FUTURO', 'EXERCICIOS')

for p in palavras:
    print(f'Na palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print()
