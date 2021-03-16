# this program plots a histogram of the salaries from (lab 8.1)
# author: Ka Ling Ip

import numpy as np #Q.1
import matplotlib.pyplot as plt

np.random.seed(1) #Q.2
randomSalaries = np.random.randint (20000,80000,100) #Q1
#print (randomSalaries)

salariesPlus = randomSalaries + 5000  #Q.3
#print (salariesPlus)

salariesInc = salariesPlus * 1.05 #Q.4
#print (salariesInc)

plt.hist(randomSalaries)
plt.show()