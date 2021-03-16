# This Program calls the function create in 6.2, and create 2 more functions from the choice
#Author: Ka Ling IP

def menu(): #create a function called menu which has 3 options
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input ("Type one letter (a/v/q):").strip() #to get rid of excess space from user input
    return choice

def doAdd(): #create a function, activate when user typed a
    print ("in adding")

def doView(): #create a function, activate when user typed v
     print ("in viewing")


if choice == "a":
    def doAdd():
        
elif choice == "v":
    def doView():

elif choice == "q":
        
else:
    print ("Please type a/v/q")
