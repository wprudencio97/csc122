# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("DB_fieldDescriptions.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 

i = 0
list=[]
while i < sheet.nrows:
    cell =  sheet.row_values(i)
    list.append(cell)
    i += 1

for data in list:
    print(data[0],data[1])

#print(list[1][1])