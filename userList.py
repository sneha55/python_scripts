import math

names = input("Enter Names : ")
listOfNames = []
totalLength =0
totalNames =0
while names.upper() != "END":
    listOfNames.append(names)
    totalLength = totalLength + len(names)
    names = input("Next : ")

totalNames = len(listOfNames)
if totalLength != 0:
    averageLength = (totalLength/totalNames)
    averageLength = math.ceil(averageLength);

for i in listOfNames:
    if len(i) > averageLength :
        print(i)



