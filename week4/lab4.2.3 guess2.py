# prompts the user to guess a number, until the user gets the right number
# give hint for the guess
# Author: Ka Ling Ip

rightAnswer = 30 # set the right asnwer
value = int(input("Please guess the number:")) # ask user for a number
while value != rightAnswer:
    if value > rightAnswer:
        print("Too high") #give hint by comparing user input and the right answer
    else:
        print("Too low")
    value = int(input("Please guess again:"))

print ("Well done! Yes the number is {}".format(rightAnswer)) #program ends when user input the right one