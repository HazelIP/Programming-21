# this program plots the function y=x**2
# author: Ka Ling Ip

import matplotlib.pyplot as plt
import numpy as np

#xpoints = np.random.randint (1,10,5) [not this as it create a wierd plot]
xpoints = np.array(range(1,101)) # create a line plot
ypoints = xpoints **2 # the function y=x**2
plt.plot (xpoints,ypoints)
plt.show()