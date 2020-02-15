import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


df = pd.read_excel('DB_fieldDescriptions.xlsx', sheet_names='vehicleID', index_col=0)
df.head()

print(df)

#for model in df.Model:
    #print(model)

