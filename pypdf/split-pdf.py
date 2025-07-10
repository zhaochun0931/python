from pypdf import PdfReader, PdfWriter
import os

def split_pdf(input_pdf_path, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    reader = PdfReader(input_pdf_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_path = os.path.join(output_dir, f"page_{i + 1}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Saved: {output_path}")

# Example usage
split_pdf("input.pdf", "output_pages")
