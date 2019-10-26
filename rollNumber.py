from typing import Any, Union

roll = 1
totalMarksDict ={}
countSubjectDict = {}
while roll != 0:
    roll = input("Please enter roll : ")
    if roll.isdigit():
        roll = int(roll)
    else:
        print("Invalid Number")
        break
    if roll == 0:
        continue
    marks = input("Please enter marks : ")
    if marks.isdigit():
        marks = float(marks)
    else:
        print("Invalid Number")
        break
    if roll in totalMarksDict:
        totalMarksDict[roll] = totalMarksDict[roll] + marks
        countSubjectDict[roll] = countSubjectDict[roll]+1
    else:
        totalMarksDict[roll] = marks
        countSubjectDict[roll] = 1
for index,value in totalMarksDict.items():
    print("roll ", index, "Total Marks :", value)
    total = countSubjectDict[index]
    averageMarks = value/total
    print("roll ", index, "Average Marks :", averageMarks)