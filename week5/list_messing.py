# just to test and mess around with list

list = [2,3,4,]
list.append(99)
biggerList = list + [10,11,12]
# print (len(biggerList))
aList = [2,3.5, False, "hi",[list],{}]

# print (aList[-2::-2])

#test pop(0)
for x in biggerList:
    print("element in list ", x)
testPop = biggerList.pop(0) 
print (testPop)
