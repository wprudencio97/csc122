import xlrd
import sqlite3

def main():
    #open the field description workbook
    workBook = xlrd.open_workbook("DB_fieldDescriptions.xlsx")
    #send each sheet to the readData function
    for sheet in workBook.sheets():
        readData(sheet)

    workBook2 = workBook = xlrd.open_workbook("vehicleData.xlsx")
    for sheet in workBook2.sheets():
        createData(sheet)

def readData(sheet):
    sheet.cell_value(0, 0) 
    #create a long string to store the data
    longString = ""

    #iterate every row
    for i in range(1, sheet.nrows):
        cell =  sheet.row_values(i)
        longString = longString + " " + str(cell[0]) + " " + str(cell[1]) + ","

    #remove the last character from the longString    
    longString = longString[:-1]
    #Use the sheet name and longString to create the database tables
    createDB(sheet.name, longString)


def createDB(sheetName, longString):
    
    # Create a connection.
    conn = sqlite3.connect('vehicle.db')
    # Create a cursor
    c = conn.cursor()
    # Drop the table if already exists
    c.execute(f"DROP TABLE IF EXISTS {sheetName}")
    # Create a table
    c.execute(f"CREATE TABLE {sheetName}({longString})" )
    # Save (commit) the changes
    conn.commit()
    # Close the connection.
    conn.close()

def createData(sheet):
    sheet.cell_value(0, 0) 
    #get the sheet name and change to reflect its database table
    sheetName = sheet.name
    if sheetName == "vehicleData":
        sheetName = "vehicleTable"
    elif sheetName == "maintenanceData":
        sheetName = "maintenanceTable" 
    

    #get the name of each column
    columnNames = getString(sheet.row_values(0))
    columnCount = getCount(sheet.row_values(0))

    #iterate every row
    for i in range(1, sheet.nrows):
        # Create a connection.
        conn = sqlite3.connect('vehicle.db')
        # Create a cursor
        c = conn.cursor()

        # insert the values into the database
        values = sheet.row_values(i)
        sql = f"INSERT INTO {sheetName} ({columnNames}) VALUES ({columnCount})"
        c.execute(sql, values)

        #Save (commit) the changes
        conn.commit()
        #Close the connection.
        conn.close()


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

main()#run the program