# Método de Newton-Raphson

import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx  = lambda x: x**3 + 2*(x**2) + 10*x - 20
dfx = lambda x: 3*(x**2) + 4*x +10
x = np.linspace(-10,10,1000);
x0 = 6
error = 0.001

# PROCEDIMIENTO
tabla = []
deltax = 0.002
xi = x0
fi = fx(x)
plt.axvline(0, color='k')
plt.axhline(0, 0, color='k')
plt.plot(x,fi,'b')


while (error<deltax):
    xnuevo = xi - fx(xi)/dfx(xi)
    deltax = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,deltax])
    plt.plot(xi, fx(xi), 'go')
    plt.plot(xnuevo, 0, 'go')
    plt.plot(np.linspace(xi, xnuevo, 2), np.linspace(fx(xi), 0, 2), 'g')
    plt.plot(np.linspace(xnuevo, xnuevo, 2), np.linspace(0, fx(xnuevo), 2), 'r')
    xi = xnuevo
    print('Deltax',deltax)

# convierte la lista a un arreglo.
tabla = np.array(tabla)

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
