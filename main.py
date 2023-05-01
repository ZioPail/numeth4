import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
#from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.animation import PillowWriter
#from matplotlib.ticker import LinearLocator
#from matplotlib import cm
#import skimage
#from skimage import color, io
#from skimage.transform import downscale_local_mean
#import numba
#from numba import jit
#import os


#RETICOLO DI INTEGRAZIONE
x = 1  #range spazio
n_1=10 #discretizzo lo spazio in n_1 passi
dx_0 = x/n_1  #definisco il passo spaziale

y = 1 # #range tempo
n_2 =100 #discretizzo il tempo in n_2 passi (deve essere maggiore di n_1)
dy_0 = y/n_2 #definisco il passo temporale
v=1  #velocità dell'onda, normalizzo a 1

#Condizione di Courant-Friedrichs-Lewy ( CONTROLLO STABILITA LINEARE')
C=(v*dy_0)/dx_0
if C>1:
    print("NO")

#CONDIZIONE INIZIALE GAUSSIANA
mu=0
sigma=1
u_0=norm.pdf(x, mu, sigma) #funzione gaussiana nello spazio

#DEFINISCO L'EVOLUZIONE DELLA FUNZIONE AVANTI E INDIETRO
i=0 #indice spazio
j=0 #indice tempo
dx=i*dx_0 #definisco l'i-esimo passo spaziale 
dy=j*dy_0 #definisco il j-esimo passo temporale
u_dx_r=norm.pdf(x+dx, mu, sigma) #definisco l'evoluzion spaziale della funzione avanti
u_dx_l=norm.pdf(x+(dx-dx_0), mu, sigma) #definisco l'evoluto spaziale della funzione indietro


u=np.array([u_0])
for j in range(1,n_2,1):  #calcola l'evoluto temporale
    u_dt=(u_dx_r + u_dx_l)/2 - v*dy_0(u_dx_r - u_dx_l)/dx_0
    i=+1
    dx=i*dx_0
    np.append(u,u_dt)


    

        
#FA IL GRAFICO SURFACE
ax=plt.axes(projection="3d")
ax.set_xlabel('x', fontsize=20, rotation=0)
ax.set_ylabel('y', fontsize=20, rotation=0)
ax.set_zlabel('z', fontsize=20, rotation=0)
xg=np.arange(0,x,n_1)
yg=np.arange(0,y,n_2)
X,Y = np.meshgrid (xg,yg)
Z=u
#ax.plot_surface(X,Y,Z, cmap ='plasma', linewidth=0)
#ax.view_init(45,45) #ruota il grafico
#plt.show()
#plt.savefig("Grafici2.jpg")