from docx import Document


# Create a new Word document
doc = Document()

# Add text to the document
doc.add_paragraph('Hello, this is a sample text.')

# Save the document
doc.save('new_document.docx')
