import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x,m,b):
    y = m*x + b
    return y

# Data
KI = np.arange(0,0.11,0.01)
I = [793.8,781.0,720.0,581.5,407,355,300,291,276,210,203]
linearx = np.linspace(0,0.10, 100)
lineary = linear(linearx,-6598.18,777.027)
# Applying curve fit
popt, pcov = curve_fit(linear,KI,I)
print(popt,pcov)
# Graphing data
fig = plt.figure(figsize = (10,6))

ax = fig.add_subplot(111)
ax.scatter(KI, I , label = "Lab_Data")
ax.plot(linearx,lineary, c = "Black", label = "Best Fit: m:-6598, b:777")
ax.set_title("Quenching of Rhodamine 110 from KI")
ax.set_xlabel("[KI]")
ax.set_ylabel("Intensity (au)")
ax.legend() 

fig.savefig("Quenching _Plot")