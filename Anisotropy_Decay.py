import numpy as np
from matplotlib import pyplot as plt

def ex_decay(t,alpha,T):
    y = 0.38 * alpha * np.exp(-t/T)
    return y

x = np.linspace(0,2.5,1000)
y1 = ex_decay(x,0.99,0.2)
y2 = ex_decay(x,0.01,50)
y_tot = y1 + y2

fig = plt.figure(figsize = (10,6))
ax = plt.subplot(111)
ax.plot(x, y_tot)
ax.set_title("Anisotropic Decay HW")
ax.set_xlabel("Time (ns)")
ax.set_ylabel("Anisotropy")
fig.savefig("Anisotropic Decay HW")