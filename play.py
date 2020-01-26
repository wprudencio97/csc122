file = open("contactsData.txt", "r")

#define the lits to be used
dataList, nameList, emailList = [], [], []

#read the lines from the txt file
for line in file:
    line = line.rstrip("\n")
    dataList.append(line)

#plit the data list into the name and email lists 
for i in dataList:
    #split the name and add it to the list
    name = i.split(",")[0]
    nameList.append(name)
    #split the email and add it to the list
    email = i.split(", ")[1]
    emailList.append(email)

#print the name and email lists 
#print(nameList)
#print(emailList)

for i in nameList:
    print(i)

for i in emailList:
    print(i)

file.close()