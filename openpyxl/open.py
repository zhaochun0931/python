import openpyxl

# Load the Excel workbook
file_path = '111.xlsx'  # Replace with the path to your file

wb = openpyxl.load_workbook(file_path)

# Get the sheet names
sheet_names = wb.sheetnames

# Print the sheet names and count
print(f"The workbook contains {len(sheet_names)} sheet(s).")
print("Sheet names:", sheet_names)
