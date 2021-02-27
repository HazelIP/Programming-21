# This program stores a student name and a list of her course and gradse in a dict
# then print out her data (number of course could change)
# Author: Ka Ling IP

student = { #create a dict that store student info
    "name": "Mary",
    "module": [{ #number of course could change, create a list to store
        "course": "Programming",  #create a nested dict to store each courses and grades
        "grade": "45"},
    {
        "course": "History",
        "grade": "99"}
    ]
}
print ("Student: ", student["name"])
for module in student["module"]:# do not understand
    print ("\t{}:\t{}".format(module["course"],module["grade"])) 