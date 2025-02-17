import numpy as np
from matplotlib import pyplot as plt

# Read in the data first and trim as necessary
data1 = np.genfromtxt('Lab_4_Glycine_Viscocity/R110_gly_exc470_obs560_sl10,5_780V_gfactor_good.csv', delimiter = ',', skip_header = 1, skip_footer = 337, names = True)

print(data1.dtype.names)
print(np.average(data1["Intensity_au_4"])/np.average(data1["Intensity_au_3"]))


#creating figures
fig = plt.figure(figsize = (20,15))
ax = fig.add_subplot(121)
ax1 = fig.add_subplot(122)


#plotting each data
ax.plot(data1['Wavelength_nm_3'], data1['Intensity_au_3'], label = 'VV')
ax.plot(data1['Wavelength_nm_4'], data1['Intensity_au_4'])
ax1.plot(data1['Wavelength_nm_2'], data1['Intensity_au_2'])
ax1.plot(data1['Wavelength_nm_1'], data1['Intensity_au_1'])
ax1.plot(data1['Wavelength_nm'], data1['Intensity_au'])



#formatting figure
ax.set_title('Rhodamine 110 Excitation Data 470nm', size = 20)
ax.legend(fontsize = 'large')
ax.set_xlabel('Emission Wavelength (nm)', size = 16)
ax.set_ylabel('Intensity', size = 16)

ax.set_title("Rhodamine 110 Excitation Data 520nm", size = 20)
ax.set_xlabel("Excitation Wavelength (nm)", size = 16)
ax.set_ylabel("Intensity", size = 16)


fig.savefig('Rhodamine_VV_VH_Data')
