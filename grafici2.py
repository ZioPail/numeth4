#import matplotlib
#matplotlib.matplotlib_fname()
import matplotlib.backends
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#plt.switch_backend('TkAgg')
#import pylab 
import numpy as np
#from mpl_toolkits import mplot3d
#from matplotlib.ticker import LinearLocator
#from IPython.display import display


#print(matplotlib.get_backend())

#FA IL GRAFICO SURFACE
ax=plt.axes(projection="3d")
ax.set_xlabel('x', fontsize=20, rotation=0)
ax.set_ylabel('y', fontsize=20, rotation=0)
ax.set_zlabel('z', fontsize=20, rotation=0)
x=np.linspace(-2,2,100)
y=np.linspace(-2,2,100)
X,Y = np.meshgrid (x,y)
Z=10*np.cos(X**2+Y**2)/(3+X**2+Y**2)
fig=ax.plot_surface(X,Y,Z, cmap ='plasma', linewidth=0)
#ax.view_init(45,45) #ruota il grafico
plt.show()
#display(fig)
#pylab.show(block=False)
#plt.savefig("Grafici2.jpg")



