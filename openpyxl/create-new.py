import openpyxl

# Create a new workbook
wb = openpyxl.Workbook()

# Select the active sheet
sheet = wb.active

# Insert a value into a specific cell
sheet['A1'] = "Hello, World!"  # Insert value into cell A1

# Optionally, you can insert data into more cells:
sheet['B1'] = "This is a test"

sheet.cell(10,8).value = 400

sheet.cell(row=3, column=3).value = 300

# Save the workbook to a file
wb.save("new_excel_file.xlsx")

print("Excel file created and value inserted successfully!")
