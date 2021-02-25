# This program reads in string, strips spaces, convert to lower case, output length of input and output strings
# Author: Ka Ling Ip

#read in string
inputString = str(input("Please enter a string:"))
#strips spaces
noSpaceString = inputString.strip()
#convert to lower case
lowerString = noSpaceString.lower()
# returns length of input and output
lengthOfInput = len(inputString)
lengthOfOutput = len(lowerString)
#print messages
print("That String normalised is :" + lowerString)
print("we reduced the input string from {} to {} characters".format(lengthOfInput,lengthOfOutput))
