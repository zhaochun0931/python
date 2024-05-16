import pytesseract
from PIL import Image

# Open an image file
image = Image.open('example.png')

# Use pytesseract to recognize text in the image
text = pytesseract.image_to_string(image)

# Print the recognized text
print(text)
