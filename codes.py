import pandas as pd

# Create 2 different data sets
data_set1={(1,2,3,4),(4,5,6,7)}
data_set2={(8,9,10,11),(12,13,14,15)}
# Convert data sets into dataframe
data_frame1=pd.DataFrame(data_set1)
data_frame2=pd.DataFrame(data_set2)
# Create a new Excel sheet or replace the existing excel sheet.
writer = pd.ExcelWriter('./project1.xlsx', engine='xlsxwriter')
# Write data_frame1 to sheet df1 and data_frame2 to sheet df2
data_frame1.to_excel(writer,sheet_name ='df1',index=True)
data_frame2.to_excel(writer,sheet_name='df2',index=True)
writer.save()
