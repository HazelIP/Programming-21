# This program create a menu which allow users to choose from 3 options
# author:Ka Ling IP

def menu(): #create a function called menu which has 3 options
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input ("Type one letter (a/v/q):").strip() #to get rid of excess space from user input
    

    return choice
choice = menu ()
print ("you chose {}".format(choice))