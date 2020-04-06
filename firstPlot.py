# firstPlot.py

import numpy as np
import matplotlib.pyplot as plt

# close all previous figures
plt.close('all')

x = np.linspace(-2*np.pi , 2*np.pi, 100)
sinx = np.sin(x) # calculate sinx
plt.plot(x, sinx) #plot x on the x axis and sinx on the y axis


################ Legend ################
# label in plt.plot are displayed by the legend command
plt.legend(loc = "best")


# label and the grid
plt.xlabel("Radian") #x-label
plt.ylabel("Amplitude") #y-label

plt.grid() #show the grid

plt.show() #display the plot


