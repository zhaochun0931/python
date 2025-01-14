from openpyxl import Workbook
from openpyxl import load_workbook
import datetime

# create a new xlsx file and a default sheet
wb = Workbook()

# the first sheet is a default active sheet
ws = wb.active
print(ws)

# input the data to cell of A1
ws['A1'] = 100


# input the current datetime to A2
ws['A2'] = datetime.datetime.now()




# merge some cells
ws.merge_cells('C2:D5')


# create 5 sheets in this xlsx file
for i in range(1,5):
    wb.create_sheet(f"mysheet{i}")


# input the current datetime to the cell of C6
for i in wb.sheetnames:
    ws = wb[i]
    ws.cell(1,1).value= i

# print all the sheets names in this workbook
print(wb.sheetnames)



# save the current xlsx file
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d-%H-%M-%S")
wb.save(f"{file_name}.xlsx")
wb.save("demo.xlsx")






# open an existing xlsx file

wb = load_workbook('demo.xlsx')

for i in wb.sheetnames:
    ws = wb[i]
    print("the max column of this sheet is ", ws.max_column)
    print("the max row of this sheet is ",  ws.max_row)
    print()
