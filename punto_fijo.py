#Librerias

import numpy as np
import matplotlib.pyplot as plt

#Funciones

def puntofijo(gx, a, tolera, iteramax=15):#Unicio de la función
    i = 1
    b = gx(a)
    tramo = abs(a - b)

    while (tramo >= tolera and i<=iteramax):
        a = b
        b = gx(a)
        tramo = abs(b - a)
        i = i + 1
    respuesta = b #Retorno de la función

    #Validar respuesta

    if (i >= iteramax):
        respuesta = np.nan
    return (respuesta)

#Fin de la función

#Entadas

fx = lambda x: 2*(x**2) - x - 5
gx = lambda x: np.sqrt((x+5)/2)

a = -5 #intervalo
b = 5
tolera = 0.0001
iteramax = 15 # máximo de iteraciones
muestras = 100 #grafico
tramos = 50

#Procedimiento

respuesta = puntofijo(gx, a, tolera)
xi = np.linspace(a, b, muestras)
fi = fx(xi)
gi = gx(xi)
yi = xi

#Salidas

print(respuesta)
plt.plot(xi, fi, label='f(x)')
plt.plot(xi, gi, label='g(x)')
plt.plot(xi, yi, label='(y=x)')


if(respuesta != np.nan):
    plt.axvline(respuesta)#Linea vertical donde cruzan la funcion

plt.axhline(0, color='k')
plt.axhline(0, 0, color='k')
plt.plot(respuesta, 0, 'ro', label='raiz')
plt.title('Punto Fijo')
plt.legend()
plt.show()
