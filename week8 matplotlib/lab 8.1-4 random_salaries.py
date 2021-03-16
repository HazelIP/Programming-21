# This program makes a list called salaries that has 10 random numbers (20000-80000)
# and then “seed” the random number generator
# and then create a new array that  has the salaries plus 5000 
# and then create a new array that increases all the salaries by 5%
# Author: Ka Ling Ip

import numpy as np #Q.1
np.random.seed(1) #Q.2
randomSalaries = np.random.randint (20000,80000,10) #Q1
print (randomSalaries)

salariesPlus = randomSalaries + 5000  #Q.3
print (salariesPlus)

salariesInc = salariesPlus * 1.05 #Q.4
print (salariesInc)
