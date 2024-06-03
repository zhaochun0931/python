from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)

first_page = reader.pages[0]
text = first_page.extract_text()

print("the page of this pdf is: ", number_of_pages)
