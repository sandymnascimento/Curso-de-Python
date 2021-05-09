frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)
comp = frase
tam = len(frase) - 1
# inverso = frase[::-1] copiaria a frase "de tras pra frente" na str inverso.
# Solução do professor inclui preenchimento e comparação direta (str == frase). Usarei para printar o inverso.
str = ''
for c in range(len(frase) - 1, -1, -1):
    str += frase[c]
print(f'A frase digitada foi {frase}, e seu inverso é {str}.')

# Abaixo esta a minha solução:
for c in range(0, len(frase)):
    if frase[c] == comp[tam]:
        tam -= 1
    else:
        print('A frase não é um palíndromo.')
        break
if tam == -1:
    print('A frase é um palíndromo.')

