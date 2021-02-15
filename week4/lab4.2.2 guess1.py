# prompts the user to guess a number, until the user gets the right number
# Author: Ka Ling Ip

# set the right asnwer
rightAnswer = 30
# ask user for a number
value = int(input("Please guess the number:"))
while value != rightAnswer:
    print("Wrong") #if it's not the right answer prompt again
    value = int(input("Please guess again:"))
print ("Well done! Yes the number is 30") #program ends when user input the right one