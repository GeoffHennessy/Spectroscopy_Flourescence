import numpy as np
from matplotlib import pyplot as plt
data = np.genfromtxt('R110_eth_exWavelength470_slits55_V900.csv', delimiter = ',', skip_header = 1, skip_footer = 114, names = True)

print(data.dtype.names)
x1Vals = data['Wavelength_nm']
x2Vals = data['Wavelength_nm_1']
x3Vals = data['Wavelength_nm_2']

y1Vals = data['Intensity_au']
y2Vals = data['Intensity_au_1']
y3Vals = data['Intensity_au_2']
y4Vals = 1/3*(y1Vals + 2* y2Vals)


#creating figures
fig = plt.figure(figsize = [10,6])
ax = fig.add_subplot(111)

#plotting each data
ax.plot(x1Vals,y1Vals, label = 'VV')
ax.plot(x2Vals,y2Vals, c = 'green', label = 'VH')
ax.plot(x3Vals,y3Vals, c = 'orange', label = 'MA')
ax.plot(x3Vals,y4Vals, c = 'black', linestyle = 'dashed', label = 'calculated MA')

#formatting figure
ax.set_title('Rhodamine 110 Excitation Data', size = 20)
ax.legend(fontsize = 'large')
ax.set_xlabel('Excitation Wavelength (nm)', size = 16)
ax.set_ylabel('Intensity', size = 16)
fig.savefig('Rhodamine_VV_VH_Data')
