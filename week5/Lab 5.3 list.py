# This program generate 10 random number from 0-100 in a queue(list)
# output all values in queue, then take 1 number from the queue 1 at a time, print it
# the current number is still in the queue [command pop(0)]
# Author: Ka Ling Ip

import random
queue = [] # create a list to hold 10 random numbers range 0-100
for n in range (0,10): # generate 10 random number 0-100
    queue.append(random.randint(0,100)) # put the generated number in the list
print ("queue is ", queue) #output all values in the queue

while len(queue) != 0: #while loop to pop value to currentNumber from queue and print
    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {}".format(currentNumber,queue))

print ("the queue is now empty") 
