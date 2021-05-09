print('=' * 82)
print('Digite o valor dos segmentos de reta e descubra se é possível formar um triângulo.')
print('=' * 82)
a = int(input('Digite o valor do lado A: '))
b = int(input('Digite o valor do lado B: '))
c = int(input('Digite o valor do lado C: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos análisados podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo.')