import xlrd
book = xlrd.open_workbook("vehicleData.xlsx")
for sheet in book.sheets():
    print(sheet.name)