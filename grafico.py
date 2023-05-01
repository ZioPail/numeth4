import matplotlib as mp
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
import math

#GRAFICO 2D
#plt.xlim(-3, 3) #definisce l'intervallo dell'asse x
#plt.xlabel("x") #definisce il nome dell'asse x
#plt.ylim(0, 0.40) #definisce l'intervallo dell'asse y
#plt.ylabel("u") #definisce il nome dell'asse y
#plt.title("Grafico") #definisce il titolo
#plt.grid(color="black", linestyle='dotted', linewidth=1) #inserisce una griglia
#plt.plot(x,u, marker=".", linestyle="dotted", linewidth =0.1,markersize=1, color ="black") #fa il grafico 2D di u

#PACCHETTO GAUSSIANO
#mu=0
#sigma=1
#x=np.linspace(-10,10,1000) #crea un array che va da -1 a 1 in 100 passi
#u_x=norm.pdf(x, mu, sigma) #funzione gaussiana


#GRAFICO A LINEE 3D
#ax = plt.axes(projection ='3d') 
#ax.plot3D(x,y,(u_x)*(u_y),'green')

#GRAFICO A DISPERSIONE SEMPRE A LINEE
#ax = plt.axes(projection ='3d')
#z = np.linspace(0, 1, 100)
#x = z * np.sin(25 * z)
#y = z * np.cos(25 * z)
#ax.scatter(x, y, z)

ax = plt.axes(projection ='3d')
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X,Y=np.meshgrid(x,y)
Z=10*np.cos(X**2+Y**2)/(3+X**2+Y**2)
ax.plot_surface(X,Y,Z)
#ax.view_init(45,45) #ruota il grafico

#GRAFICO2 3D per superfici
#ax = plt.axes(projection ='3d')
#x = np.linspace(-2, 2, 1000)
#y = np.linspace(-2, 2, 1000)
#X,Y=np.meshgrid(x,y)
#Z=10*np.cos(X**2+Y**2)/(3+X**2+Y**2)
#ax.plot_wireframe(X,Y,Z)




plt.savefig("Grafico.jpg") #salva la figura come Grafico.png
plt.show()
