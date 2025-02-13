import numpy as np
from matplotlib import pyplot as plt

data = np.genfromtxt('012325+R110+Abs+Geoffrey.csv', delimiter= ',', skip_header=1, skip_footer=36, names = True, autostrip=True)


fig = plt.figure(figsize=(20,16))
ax = fig.add_subplot(111)
ax.plot(data['Wavelength_nm'],data['Abs'], label = 'Absorbtion Spectra')
ax.set_title("Absorbtion Spectra: Rhodamine", size = 36)
ax.set_xlabel('Wavelength (nm)',size = 20)
ax.set_ylabel('Absorbtion', size = 20)
ax.tick_params(labelsize = 16)

ax.scatter(501,0.0777, c='red', s = 150, label = "Extinction coefficient: 0.0777")
ax.legend(fontsize = 16, loc = 'upper left')
fig.savefig("fig_1")
