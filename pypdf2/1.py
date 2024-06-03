# this is a very simple demo to print the page number of the pdf

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter



reader = PdfReader("example.pdf")
writer = PdfWriter()

number_of_pages = len(reader.pages)

first_page = reader.pages[0]
text = first_page.extract_text()

print("the page of this pdf is: ", number_of_pages)


first_page.mediabox.lower_left = (400,400)
first_page.mediabox.upper_right = (800,800)
writer.add_page(first_page)
writer.write("2.pdf")
