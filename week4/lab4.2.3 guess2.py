# prompts the user to guess a number, until the user gets the right number
# give hint for the guess
# Author: Ka Ling Ip

# set the right asnwer

rightAnswer = 30
# ask user for a number
value = int(input("Please guess the number:"))
while value != rightAnswer:
    if value > rightAnswer:
        print("Too high") #give hint for the right answer
    else:
        print("Too low")
    value = int(input("Please guess again:"))

print ("Well done! Yes the number is {}".format(rightAnswer)) #program ends when user input the right one