# This program tells if the number user entered is even or odd. 
# # Author: Ka Ling Ip

# ask user to enter a number num = int(input("Enter a number:"))
num = float(input("Enter a number:"))

# if a number is even, it can be divided by 2 with remainder = 0, 
# otherwise is odd.
if (num % 2) == 0: 
    print ("{} is an even number".format(num))
else: 
    print ("{} is an odd number".format(num))