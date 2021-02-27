# This program keeps reading numbers until the user enters a 0. (the program should append each of them into a list)
# then print out each of the numbers entered and the average of them. (Use a list)
# Author: Ka Ling Ip 

allNum = [] #create a list to contain all num
num = int(input ("enter number (0 to quit):")) #ask user to input a number 
while num != 0: #program stop reading in number when user enter 0
    allNum.append(num) #if input not 0, put in list
    num = int(input ("enter number (0 to quit):")) #then prompt input again

for value in allNum: #regarding the list that contains all num
    print(value) #print all the input
average = float(sum(allNum)/len(allNum)) # calculate average of input

print("The average is {}".format(average))