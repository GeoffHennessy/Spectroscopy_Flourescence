import numpy as np
from matplotlib import pyplot as plt

def ex_decay(t,alpha,T):
    y = 0.38 * alpha * np.exp(-t/T)
    return y

# Setting initial conditions and lists
alpha1 = 0.99
alpha2 = 0.01 
y_tot = []

x = np.linspace(0.0,2.5,1000)
for i in range(len(x)):
    y1 = ex_decay(x[i],alpha1,0.2)
    y2 = ex_decay(x[i],alpha2,50)
    y_tot.append(y1+y2)

    alpha1 = y1 / y_tot[i]
    alpha2 = y2 / y_tot[i]

fig = plt.figure(figsize = (10,6))
ax = plt.subplot(111)
ax.plot(x, y_tot)
ax.set_title("Anisotropic Decay HW")
ax.set_xlabel("Time (ns)")
ax.set_ylabel("Anisotropy")
fig.savefig("Anisotropic Decay HW")