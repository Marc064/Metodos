# Método Secante

import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx  = lambda x: x**3 + 2*(x**2) + 10*x - 20
x = np.linspace(-10,10,1000)
x0 = 6
x1 = 5
error = 0.001

# PROCEDIMIENTO
tabla = []
deltax = 0.002
xi = x1
xi1 = x0
fi = fx(x)
plt.axvline(0, color='k')
plt.axhline(0, 0, color='k')
plt.plot(x,fi,'c')
while (error<deltax):

    xnuevo = xi - (fx(xi) * (xi-xi1))/(fx(xi)-fx(xi1))
    deltax = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,deltax])
    plt.plot(xi, fx(xi), 'go')
    plt.plot(xi1, fx(xi1), 'go')

    plt.plot(np.linspace(xi, xi1, 2), np.linspace(fx(xi), fx(xi1), 2), 'g')

    xi1 = xi
    xi = xnuevo

    print('Deltax',deltax)

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print(['xi', 'xnuevo', 'deltax'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',deltax)
if(xi != np.nan):
    plt.axvline(xi)

plt.plot(xi,0,'ro')
plt.show()
