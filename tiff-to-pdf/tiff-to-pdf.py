import os
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


def convert_all_tiffs_in_directory():
    try:
        # Get the current directory
        current_dir = os.getcwd()

        # List all files in the current directory
        files = os.listdir(current_dir)

        # Filter for TIFF files
        tiff_files = [f for f in files if f.endswith('.tif') or f.endswith('.tiff')]

        # Iterate over TIFF files and convert each one
        for tiff_file in tiff_files:
            tiff_path = os.path.join(current_dir, tiff_file)
            pdf_file = os.path.splitext(tiff_file)[0] + '.pdf'
            pdf_path = os.path.join(current_dir, pdf_file)

            # Convert TIFF to PDF
            convert_tiff_to_pdf(tiff_path, pdf_path)

    except Exception as e:
        print(f"Error converting TIFF files in directory: {e}")


# Call the function to convert all TIFF files in the current directory to PDF
convert_all_tiffs_in_directory()
