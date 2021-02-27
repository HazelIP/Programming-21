# This program generate 10 random number (0-100), 
# print all the 10 random numbers out and then print top 3 numbers

import random #to generate random numbers, this block is new thing, do research
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

allNum = [] # a variable to store the 10 random numbers
for i in range (0,10): # generate 10 random numbers in range 0-100 and put them in list
    allNum.append(random.randint(0,100))
print ("10 random numbers \t {}".format(allNum))
listNum = allNum.copy()
print (listNum.sort(reverse=True))