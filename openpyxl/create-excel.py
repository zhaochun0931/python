from openpyxl import Workbook
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


# input the value to the cell
ws.cell(row=3, column=3).value = 300
ws.cell(10,8).value = 400



# print all the sheets names in this workbook
print(wb.sheetnames)



# save the current xlsx file
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d-%H-%M-%S")
wb.save(f"{file_name}.xlsx")
