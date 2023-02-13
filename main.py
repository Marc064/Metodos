#Librerias

import numpy as np
import matplotlib.pyplot as plt

#Funciones

def cuadrado(valor):
    r = valor ** 2
    return r

#Entradas

print('Digite un valor')
valor = int(input())

#Procedimiento

resultado = cuadrado(valor)

x = np.linspace(-5, 5, 1000)
y = cuadrado(x)

#Salidas

print(f"{valor} al cuadrado es {resultado}")

plt.plot(x, y, 'r')
plt.title('Cuadrado de un valor')
plt.show()#Permite mostrar la grafica de lo definido