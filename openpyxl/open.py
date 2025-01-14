import openpyxl

# Load the Excel workbook
file_path = '111.xlsx'  # Replace with the path to your file

wb = openpyxl.load_workbook(file_path)

# Get the sheet names
sheet_names = wb.sheetnames

# Print the sheet names and count
print(f"The workbook contains {len(sheet_names)} sheet(s).")
print("Sheet names:", sheet_names)

for i in range(len(sheet_names)):
    sheet_temp_name = sheet_names[i]
    sheet = wb[sheet_temp_name]
    print(sheet_names[i], sheet.max_column, sheet.max_row)
