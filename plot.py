## Tomado del repositorio anterior

import numpy as np
import matplotlib.pyplot as plt

def grafica(datafile, plotfile, plotlabel):
    data = np.loadtxt(datafile)
    
    
    plt.figure(figsize=(14,4))
    
    plt.subplot(1,3,1)
    s = np.shape(data)
    print(s)
    n_x = s[1]
    n_t = s[0]
    plt.imshow(data, extent=[-1,1,1,0], aspect=2.0)
    plt.xlabel("N_x")
    plt.ylabel("N_iteracion")
    plt.title(plotlabel)


    plt.subplot(1,3,2)
    x = np.linspace(-1,1,n_x)
    delta_t = 1.0/n_t
    for i in range(n_t):
        if i%(n_t//9) == 0:
            plt.plot(x, data[i,:], alpha=(i+1)/n_t, color='black', label="t={:.02f}".format(i*delta_t))
    plt.xlabel("N_x")
    plt.ylabel("Error centro x10^2")
            
    plt.subplot(1,3,3)
    t = np.linspace(0,1,n_t)
    plt.plot(t, data[:,n_x//2], alpha=i/n_t, color='black')
    plt.xlabel("N_x")
    plt.ylabel("'Error convergencia x10^6'")


    plt.savefig(plotfile, bbox_inches='tight')

grafica("evolve_30_450.dat", "evolve_A.png", "$N_x=30$ ,  $N_{tc}$")
