# this program makes a list called age that has same number of random values as salaries (i.e.100)
# age range: 21-65
# make a scatter plot of this data
# author:Ka Ling Ip
import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(1) #Q.2
randomSalaries = np.random.randint (20000,80000,100) #Q1
ages = np.random.randint (21,65,100) #Q7 create a list of random ages

plt.scatter(ages, randomSalaries) #create a scatter plot
# plt.show() [comment this out to continue creating the line plot as well]

xpoints = np.array(range(1,101)) # create a line plot (Q8)
ypoints = xpoints **2 # the function y=x**2
plt.plot (xpoints,ypoints, color="yellow") #make the line a differnt color
plt.title("messing random plot") #Q9
plt.legend ("scatter", "line") #no legend
plt.xlabel ("Ages")
plt.ylabel ("Salaries")
# plt.show() [comment this out to save the plot]
plt.savefig("prettier-plot.png")