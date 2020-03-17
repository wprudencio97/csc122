import sqlite3
from tabulate import tabulate

# define the main function
def main():
    conn = sqlite3.connect("vehicle.db")
    cur = conn.cursor()

    # get the user action and call the appropriate function
    userAction = input("\nEnter (C)reate, (R)ead, (U)pdate, or (D)elete: ")

    if userAction.lower() == "c" or userAction.lower() == "create":
        tableSelection = getSelection()
        createRecord(cur, tableSelection)
    elif userAction.lower() == "r" or userAction.lower() == "read":
        getReport(cur)
    elif userAction.lower() == "u" or userAction.lower() == "update":
        tableSelection = getSelection()
        updateRecord(cur, tableSelection)
    elif userAction.lower() == "d" or userAction.lower() == "delete":
        tableSelection = getSelection()
        deleteRecord(cur, tableSelection)


    #Save (commit) the changes
    conn.commit()
    # Close the connection.
    conn.close()

def getSelection():
    #get table selection 
    tableSelection = int(input("\n1: Vehicle Table \n2: Maintenance Table \nEnter the number of the table: "))

    if tableSelection == 1:
        tableSelection = "vehicleTable"
    elif tableSelection == 2:
        tableSelection = "maintenanceTable"
    
    return tableSelection

def createRecord(cur, tableName):
    #get the rowHeaders using getTableHeaders
    rowHeaders = getTableHeaders(cur, tableName)
    #get the values to insert data to
    longString = getString(rowHeaders)
    #get the amount of values to be inserted
    valueCount = getCount(rowHeaders)

    #get the values to input
    valuesList = getValues(0, rowHeaders)

    # insert the values into the database
    values = valuesList
    sql = f"INSERT INTO {tableName} ({longString}) VALUES ({valueCount})"
    cur.execute(sql, values)

def updateRecord(cur, tableName):
    #print out the table
    printTable(cur, tableName)
    #get the ID of the record to be updated
    recordID = input("\nEnter the ID of the record to update: ")

    #used to store the row names to be updated
    updateString = ""
    #get the row headers from the table
    rowHeaders = getTableHeaders(cur, tableName)

    #loop through the row headers and add them to the updateString
    for i in range(1, len(rowHeaders)):
        updateString = updateString + " " + rowHeaders[i] + "=?, "

    #remove the extra space and the , at the end
    updateString = updateString[:-2]

    #get values to be inserted using the getValues function
    dataValues = getValues(1, rowHeaders)

    #update the record with the new information
    sqlite_update_query = f"UPDATE {tableName} SET {updateString} WHERE {rowHeaders[0]} = {recordID}"
    data = (dataValues)
    cur.execute(sqlite_update_query, data)

def deleteRecord(cur, tableName):    
    #print out the table
    printTable(cur, tableName)
    #get the recordID and delete its record
    recordID = input("\nEnter the ID of the Record to delete: ")
    rowHeaders = getTableHeaders(cur, tableName)

    sqlite_update_query = f"DELETE FROM {tableName} WHERE {rowHeaders[0]} = ?"
    cur.execute(sqlite_update_query, (recordID,))

def getReport(cur):
    dataTables = ["vehicleTable", "maintenanceTable"]

    #get the vehicleID of the vehicle for which to generate a report
    printTable(cur, dataTables[0])
    vehicleID = input("\nEnter the vehicle ID for the vehicle you which to generate a report: ")

    #find the vehicle details from the vehicle table
    cur.execute(f"SELECT * FROM {dataTables[0]} WHERE vehicleID={vehicleID}")
    vehicleDetails = cur.fetchall()

    #get the table headers
    vehicleTableHeaders = getTableHeaders(cur, dataTables[0])

    #print the vehicle details
    print(" ")#empty line
    print(tabulate(vehicleDetails, headers=vehicleTableHeaders))

    #find the maintenance details for the selected vehicle 
    cur.execute(f"SELECT * FROM {dataTables[1]} WHERE vehicleID={vehicleID}")
    maintenanceDetails = cur.fetchall()

    #get the table headers
    maintenanceTableHeaders = getTableHeaders(cur, dataTables[1])

    #print the vehicle details
    print(" ")#empty line
    print(tabulate(maintenanceDetails, headers=maintenanceTableHeaders))

def getTableHeaders(cur, tableName):
    cur.execute(f"SELECT * FROM {tableName}")
    colnames = cur.description
    
    #read the row headers and store them in a list
    rowHeaders =[]
    for row in colnames:
        rowHeaders.append(row[0])
    #return the rowHeaders list
    return rowHeaders

def getValues(index, list):
    valueList = []

    for i in range(index, len(list)):
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