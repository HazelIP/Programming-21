# This program takes in a float amount of dollars and returns that absolute amount in cent
# Author: Ka Ling Ip

#ask for a float number of dollars
floatDollars = float(input("Please enter an amount:"))
#converts the float dollards to cents
dollarsToCent = int(floatDollars*100)
#convert cents to absolute value
absCent = abs(dollarsToCent)
print("That amount in cent is:{}.".format(absCent))