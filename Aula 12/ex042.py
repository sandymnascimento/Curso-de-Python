a = int(input('Digite o valor do segmento de reta A: '))
b = int(input('Digite o valor do segmento de reta B: '))
c = int(input('Digite o valor do segmento de reta C: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos análisados podem formar um triângulo!')
    if a == b and a == c:
        print('O triãngulo possuirá três lados iguais, portanto será EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('O triãngulo possuirá dois lados iguais, portanto será ISÓSCELES.')
    else:
        print('O triãngulo não possuirá lados iguais, portanto será ESCALENO.')
else:
    print('Os segmentos não podem formar um triângulo.')

