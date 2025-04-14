# Alexa Mabel Lucio Mendoza #

# Librerías
import numpy as np
from random import random
import matplotlib.pyplot as plt

# Declaro variables auxiliares
l1 = []; a1=0
l=np.ones(10000) # declaro una matriz de nucleos (10000 unos)

# decaimiento
for j in range(100): #promedia 100 veces
  l=np.ones(10000);l1=[];m=0
  prom=0
  for i in range(100): # Recorre 100 segundos
    for k in range(len(l)): # hace el ciclo para todos los nucleos
      r=random() # genera un num aleatorio del 0<=x<1
      if r<=0.01 and l[k]==1: # si el num aleatorio es menor que la probabilidad r<=0.01 y ese nucleo no ha decaído antes
          l[k]-=1 # se elimina de la lista (muestra asi que ya decayó)
          m+=1
      a1=np.sum(l) #Va haciendo el promedio
    l1.append(a1/100)

# declaro una lista para el tiempo
t = np.linspace(0,100,len(l1))
#Ajuste de la curva
from scipy.optimize import curve_fit
def modelo(x,a,b):
    return a*np.exp(-b*x)

popt,pcov=curve_fit(modelo,t,l1)
model=modelo(t,*popt)

# Graficas
plt.plot(t,l1, label='N(t)')
plt.title("Cantidad promedio de núcleos inestables en el tiempo")
plt.plot(t,model,label=f'Ajuste de la curva')
plt.xlim(0,100)
plt.xlabel('t');plt.ylabel('N(t)')
plt.grid();plt.legend();plt.show()
