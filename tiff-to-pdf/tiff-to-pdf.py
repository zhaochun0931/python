from PIL import Image
from reportlab.pdfgen import canvas

def convert_tif_to_pdf(tif_path, pdf_path):
    # Open the TIF image using Pillow
    tif_img = Image.open(tif_path)

    total_pages = tif_img.n_frames

    print("the total pages of the tiff file are: ",total_pages)

    # Create a new PDF file
    c = canvas.Canvas(pdf_path, pagesize=tif_img.size)
    
    # Draw the TIF image on the PDF
    c.drawInlineImage(tif_img, 0, 0)
    
    # Save the PDF file
    c.save()

# Example usage:
tif_file = 'example.tif'
pdf_file = 'example.pdf'

convert_tif_to_pdf(tif_file, pdf_file)

