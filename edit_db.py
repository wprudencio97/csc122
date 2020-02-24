import sqlite3
from tabulate import tabulate

# define the main function
def main():
    conn = sqlite3.connect("vehicle.db")
    cur = conn.cursor()

    #get table selection 
    tableSelection = int(input("\n1: Vehicle Table \n2: Maintenance Table \nEnter the number of the table to edit:"))
    
    if tableSelection == 1:
        tableSelection = "vehicleTable"
    elif tableSelection == 2:
        tableSelection = "maintenanceTable"

    # get the user action and call the appropriate function
    userAction = input("\nEnter (C)reate, (R)ead, (U)pdate, or (D)elete: ")

    if userAction.lower() == "c" or userAction.lower() == "create":
        createRecord(cur, tableSelection)
    elif userAction.lower() == "r" or userAction.lower() == "read":
        printTable(cur, tableSelection)
    elif userAction.lower() == "u" or userAction.lower() == "update":
        updateRecord(cur, tableSelection)


    #Save (commit) the changes
    conn.commit()
    # Close the connection.
    conn.close()

def createRecord(cur, tableName):
    #get the rowHeaders using getTableHeaders
    rowHeaders = getTableHeaders(cur, tableName)
    #get the values to insert data to
    longString = getString(rowHeaders)
    #get the amount of values to be inserted
    valueCount = getCount(rowHeaders)

    #get the values to input
    valuesList = getValues(rowHeaders)

    # insert the values into the database
    values = valuesList
    sql = f"INSERT INTO {tableName} ({longString}) VALUES ({valueCount})"
    cur.execute(sql, values)

def updateRecord(cur, tableName):
    #print out the table
    printTable(cur, tableName)
    #get the ID of the record to be updated
    recordID = input("\nEnter the ID of the record to update: ")

    updateString = ""

    rowHeaders = getTableHeaders(cur, tableName)

    for i in range(1, len(rowHeaders)):
        updateString = updateString + "SET " + rowHeaders[i] + "=?, "
    

    updateString = updateString[:-2]
    print(updateString)

    dataValues = getValues(rowHeaders)
    dataValues = getString(dataValues)
    

    #update the record with the new information
    sqlite_update_query = f"UPDATE {tableName} {updateString} WHERE {rowHeaders[0]} = {recordID}"
    data = (dataValues)
    print(data)
    cur.execute(sqlite_update_query, data)

def getTableHeaders(cur, tableName):
    cur.execute(f"SELECT * FROM {tableName}")
    colnames = cur.description
    
    #read the row headers and store them in a list
    rowHeaders =[]
    for row in colnames:
        rowHeaders.append(row[0])
    #return the rowHeaders list
    return rowHeaders

def getValues(list):
    valueList = []

    #for i in list:
     #   i = input(f"Enter the {i}: ")
      #  valueList.append(i)
    
    for i in range(1, len(list)):
        i = input(f"Enter the {list[i]}: ")
        valueList.append(i)

    return valueList 

def printTable(cur, tableName):
    cur.execute(f"SELECT * FROM {tableName}")
    rows = cur.fetchall()
    colnames = cur.description

    #read the row headers and store them in a list
    rowHeaders =[]
    for row in colnames:
        rowHeaders.append(row[0])
    
    #print the table
    print("")#empty line
    print(tabulate(rows, headers=rowHeaders))

def getString(list):
    stringData = ""
    for i in list:
        stringData = stringData + "," + str(i)

    #remove the first character(,) from stringData    
    stringData = stringData[1:]

    return stringData

def getCount(list):
    stringCount = "?"

    for i in range(1,len(list)):
        stringCount = stringCount + ",?"

    return stringCount


main() #run the program