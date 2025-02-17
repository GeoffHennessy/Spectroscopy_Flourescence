import numpy as np
from matplotlib import pyplot as plt

# Read in the data first and trim as necessary
data1 = np.genfromtxt('Lab_3_G_Factor_Correction/R110_520nMEm_800V_5-5_Geoffrey.csv', delimiter = ',', skip_header = 1, skip_footer = 77, names = True)

print(data1.dtype.names)
ma = 1/3*(data1["Intensity_au"] + 2 * data1["Intensity_au_1"])
ma_Corrected = 1e-8 * ma ** 3 + 6e-6 * ma ** 2 - .0114 * ma + 3.6128

#creating figures
fig = plt.figure(figsize = (20,15))
ax = fig.add_subplot(111)


#plotting each data
ax.plot(data1['Wavelength_nm'], data1['Intensity_au'], label = 'VV')
ax.plot(data1['Wavelength_nm_1'], data1['Intensity_au_1'], c = 'green', label = 'VH')
ax.plot(data1["Wavelength_nm"], ma, label = "ma (uncorrected)")
ax.plot(data1["Wavelength_nm"], ma_Corrected, linestyle = "dashed", label = "ma (corrected)", c = "black")



#formatting figure
ax.set_title('Rhodamine 110 Excitation Data 470nm', size = 20)
ax.legend(fontsize = 'large')
ax.set_xlabel('Emission Wavelength (nm)', size = 16)
ax.set_ylabel('Intensity', size = 16)

ax.set_title("Rhodamine 110 Excitation Data 520nm", size = 20)
ax.set_xlabel("Excitation Wavelength (nm)", size = 16)
ax.set_ylabel("Intensity", size = 16)


fig.savefig('Rhodamine_VV_VH_Data')
