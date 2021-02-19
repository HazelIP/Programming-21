# this program stores months in a tuple, and print out summer months one at a time
# author: Ka Ling Ip

# defining variables
months = ("Januray","February","March","April","May","June",
"July","August","September","October","November","December")
Summer = months [4:7] #May,June,July has the index no 4, 5, 6 respectively
# to print them out one at a time use for loop
for month in Summer:
    print (month)