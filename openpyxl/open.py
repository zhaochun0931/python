import openpyxl

# Load the Excel workbook
file_path = '111.xlsx'  # Replace with the path to your file

wb = openpyxl.load_workbook(file_path)

# Get the sheet names
ws = wb.sheetnames

# Print the sheet names and count
print(f"The workbook contains {len(ws)} sheet(s).")
print("Sheet names:", ws)

for i in range(len(ws)):
    sheet_temp_name = ws[i]
    sheet = wb[sheet_temp_name]
    print(ws[i], sheet.max_column, sheet.max_row)







# wb_new = openpyxl.Workbook()
# sheet_new = wb_new.active


for i in ws:
    my_ws = wb[i]
    print(my_ws)
    my_column = my_ws.max_column
    my_row = my_ws.max_row

    print(my_ws, my_row, my_column)


for i in range(len(ws)):
    print(i)

for i in range(len(ws)):
    print(ws[i])



