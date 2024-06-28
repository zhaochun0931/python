from PIL import Image
from reportlab.pdfgen import canvas


def convert_tiff_to_pdf(tiff_path, pdf_path):
    try:
        # Open the TIFF file
        tiff_img = Image.open(tiff_path)

        # Create a new PDF file
        c = canvas.Canvas(pdf_path)

        # Iterate over each page in the TIFF
        for i in range(tiff_img.n_frames):
            # Select the current page
            tiff_img.seek(i)

            # Convert the current page to RGB mode (if not already in RGB)
            rgb_img = tiff_img.convert('RGB')

            # Determine the dimensions of the page
            width, height = rgb_img.size

            # Draw the TIFF image on the PDF
            c.setPageSize((width, height))
            c.drawInlineImage(rgb_img, 0, 0, width=width, height=height)

            # Add a new page for the next frame (if there are more frames)
            if i < tiff_img.n_frames - 1:
                c.showPage()

        # Save the PDF file
        c.save()

        print(f"PDF successfully created: {pdf_path}")

    except Exception as e:
        print(f"Error converting TIFF to PDF: {e}")


# Example usage:
tif_file = 'example.tif'
pdf_file = 'example.pdf'

convert_tiff_to_pdf(tif_file, pdf_file)
