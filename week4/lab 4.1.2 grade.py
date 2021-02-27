# This program print a student's corresponding grade based on the student's % marks
# author: Ka Ling IP

grade = int(input("Enter the percentage:"))
if grade < 40:
    print("fail")
elif grade>=40 and grade<49:
    print ("pass")
elif grade>=50 and grade <59:
    print ("Merit 2")
elif grade>=60 and grade<69:
    print ("Merit 1")
else:
    print ("Distinction")
    