# This program print a student's corresponding grade based on the student's % marks
# Author: Ka Ling IP

#should actually use float instaed of int because of %
grade = float(input("Enter the percentage:"))
#to make sure the % entered is valid
if grade < 0 or grade > 100:
    print("Pleaes enter a valid percentage:") 
if grade < 40: 
    print("fail")
elif grade>=40 and grade<=49: 
    print ("pass")
elif grade>=50 and grade <=59: 
    print ("Merit 2")
elif grade>=60 and grade<=69: 
    print ("Merit 1")
else: print ("Distinction") # for 70-100%