selection = input("1.Count of common characters in each string.\n 2.Display common characters in all strings \n 3.Exit \n")
if not selection.isdigit():
    print("Invalid Number")
    exit()
if int(selection) > 3 or int(selection) < 0 :
    print("Invalid Selection")
    exit()
if selection == "3":
    exit()
names = input("Enter Names : ")
listOfNames = []
while names.upper() != "END":
    listOfNames.append(names)
    #totalLength = totalLength + len(names)
    names.strip();
    listOfName = list(names)
    names = input("Next : ")

if selection == "1":

    for j in listOfNames:
        cnt =0
        dictName = {}
        for i in listOfName:
            cnt = j.count(i)
            if i in dictName:
                #dictName[i] = cnt
                #print("string : ", j, "- character ", i, "count ", cnt)
                continue
            else:
                dictName[i] = cnt
                print("string : ", j, "- character ", i, "count ", cnt)
else :
    for i in listOfName:
        count =0
        for j in listOfNames:
            if i in j :
                count = count +1
            else :
                break
        if count == len(listOfNames):
            print("common characters", i)



