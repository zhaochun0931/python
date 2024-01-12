import re
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from copy import copy



wb = openpyxl.load_workbook("007.xlsx")


ws = wb.active


# display the max row of this sheet
total_row = ws.max_row
print("the total numbers of the row are ", total_row)

for student_row in range(1,total_row+1):
    # get the student name
    txt = ws.cell(student_row,1).value

    if txt is not None:
        # x = re.findall("姓名:(.*)\s",str(txt))
        x = re.match("姓名：(.*)\s考号.*",str(txt))
        if x:
            student_name = x.group(1)
            print("the student name is ", student_name," and the row number is: ",student_row)
            # print(x.group(1))


            # create a new sheet for each student
            wb_new = Workbook()
            ws_new = wb_new.active

# display student name on the first row

            ws_new.merge_cells('A1:D1')

            ws_new.cell(1,1).value = ws.cell(student_row,1).value
            ws_new.cell(1,1).font = copy(ws.cell(student_row,1).font)
            ws_new.cell(1, 1).alignment = copy(ws.cell(student_row, 1).alignment)
            ws_new.row_dimensions[1].height = ws.row_dimensions[student_row].height + 15
            # ws_new.column_dimensions['A'].width = ws.column_dimensions['A'].width + 10



            for select_range_row in range(1,10):

                # print the row number
                # print(select_range_row)

                # get the current height of the row
                my_row_height = ws.row_dimensions[student_row + select_range_row].height
                print("the row height is ", my_row_height)

                tmp_row = select_range_row + 1
                print("the tmp row number is ", tmp_row)

                # ws_new.row_dimensions[tmp_row] = ws.row_dimensions[student_row + select_range_row]
                # print(my_row.height)

                ws_new.row_dimensions[tmp_row].height = my_row_height
                # ws_new.row_dimensions[tmp_row].height = my_row_height


                for select_range_column in range(1,5):
                    # print the column width
                    # print("the column width is ", ws.column_dimensions['D'].width)
                    ws_new.cell(select_range_row+1,select_range_column).value = ws.cell(student_row+select_range_row,select_range_column).value
                    ws_new.cell(select_range_row+1,select_range_column).alignment = Alignment(wrapText=True,horizontal='center',vertical='center')



                    # ws_new.row_dimensions[select_range_row + 1].height = ws.row_dimensions[student_row + select_range_row].height

                    # ws_new.row_dimensions[select_range_row + 1].height = ws.row_dimensions[student_row + 1].height
                    #
                    if select_range_column == 4:
                        # ws_new.row_dimensions[select_range_row + 1].height = ws.row_dimensions[4].height
                        ws_new.column_dimensions['D'].width = ws.column_dimensions['D'].width + 10
                        # ws_new.cell(select_range_row+1,select_range_column).alignment = Alignment(wrapText=True,horizontal='center',vertical='center')




            wb_new.save(f"{student_name.strip()}.xlsx")

