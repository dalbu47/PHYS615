import numpy as np
import matplotlib.pyplot as plt

g = 1
Vter = [0.3, 1, 3, 9999999]
Vlist = ["Vter = 0.3 m/s", "Vter = 1 m/s", "Vter = 3 m/s", "Vter = large"]
Vxo = 1
Vyo = 1
t = np.linspace(0,3,10000)
fig, (ax1,ax2,ax3)=plt.subplots(3,1, figsize=(8,10))
fig.subplots_adjust(hspace=0.625)
for i in range(len(Vter)):
    xt = Vxo*Vter[i]*(1 - np.exp(-t/Vter[i]))
    ax1.plot(t, xt, label=Vlist[i])
    ax1.legend(fontsize=7)
    ax1.set_title('X(t) with Linear Drag',fontsize=15)
    ax1.set_xlabel('t', fontsize=10)
    ax1.set_ylabel('x', fontsize=10)
    yt = (Vyo+Vter[i])*Vter[i]*(1 - np.exp(-t/Vter[i])) - Vter[i]*t
    ax2.plot(t, yt, label=Vlist[i])
    ax2.legend(fontsize=7)
    ax2.set_title('Y(t) with Linear Drag',fontsize=15)
    ax2.set_xlabel('t', fontsize=10)
    ax2.set_ylabel('y', fontsize=10)
    yx = ((Vyo+Vter[i])/(Vxo))*xt + Vter[i]*Vter[i]*np.log(1-(xt/(Vxo*Vter[i])))
    ax3.plot(xt, yx, label=Vlist[i])
    ax3.legend(fontsize=7)
    ax3.set_title('Y(x) with Linear Drag',fontsize=15)
    ax3.set_xlabel('x', fontsize=10)
    ax3.set_ylabel('y', fontsize=10)

#%%
