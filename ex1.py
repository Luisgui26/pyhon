a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

def bhaskara():
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        frase += 'Não há raízes'
    elif delta == 0:
        frase += 'Ambas as raízes são iguais a '
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        frase += f'x1 = {x1}   x2 = {x2}'
    xv = -b/(2 * a)
    yv = -delta/(4 * a)
    frase += f' e o vértice está em xv = {xv} e yv = {yv}'
    return frase
a = 1
b = -5
c = 6
resultado = bhaskara(a, b, c)
print(resultado)

i = -10
x  = []
y = []
while i < 10:
    x.append(i)
    f = a*i**2 + b*i + c
    y.append(i)
    i += 0.01
    print(x)
    print(y)

import matplotlib as plt

plt.plot(x, y)
plt.show()




    


