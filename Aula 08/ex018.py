from math import cos, sin, tan, radians

x = float(input('Digite um ângulo: '))
print('O seno de {} é {:.2f}.' .format(x, sin(radians(x))))
print('O cosseno de {} é {:.2f}.' .format(x, cos(radians(x))))
print('A tangente de {} é {:.2f}.' .format(x, tan(radians(x))))
