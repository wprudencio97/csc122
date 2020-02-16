import xlrd
import sqlite3

  
def main():
    #open the workbooks
    workBook = xlrd.open_workbook("DB_fieldDescriptions.xlsx")
    for sheet in workBook.sheets():
        readData(sheet)

    #send file and sheet info to the readData function
    #sheetOne = readData(excelFile = "DB_fieldDescriptions.xlsx", sheetIndex = 0) 
    #sheetTwo = readData(excelFile = "DB_fieldDescriptions.xlsx", sheetIndex = 1)

    #send the list data to the createDB function
    #createDB(sheetOne)
    #createDB(sheetTwo)

def readData(sheet):
    sheet.cell_value(0, 0) 

    longString = ""
    for i in range(1, sheet.nrows):
        cell =  sheet.row_values(i)
        longString = longString + " " + str(cell[0]) + " " + str(cell[1]) + ","
    
    createDB(sheet.name, longString)

def createDB(sheetName, longString):
    longString = longString[:-1]
    print(longString)
    # Create a connection.
    conn = sqlite3.connect('vehicle.db')
    # Create a cursor
    c = conn.cursor()
    c.execute(f"DROP TABLE IF EXISTS {sheetName}")
    # Create a table
    c.execute(f"CREATE TABLE {sheetName}({longString})" )
    # Save (commit) the changes
    conn.commit()

    # Close the connection.
    conn.close()


main()