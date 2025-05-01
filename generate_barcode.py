import treepoem
from PIL import ImageOps # Pillow is used by treepoem

# Standard PDF417
# https://www.hub.hr/sites/default/files/inline-files/2DBK_EUR_Uputa_1.pdf
data_to_encode = """HRVHUB30
EUR
000000000012355
ŽELJKO SENEKOVIĆ
IVANEČKA ULICA 125
42000 VARAŽDIN
2DBK d.d.
ALKARSKI PROLAZ 13B
21230 SINJ
HR1210010051863000160
HR01
7269-68499637766-00019
COST
Troškovi za 1. mjesec"""

try:
    # Generate the barcode
    image = treepoem.generate_barcode(
        barcode_type='pdf417',
        data=data_to_encode,
        scale=4,
        # options={},
    )

    # Add padding (treepoem doesn't add much by default)
    image = ImageOps.expand(image, border=10, fill='white')

    # Save the image
    file_path = 'barcode.png'
    image.convert('1').save(file_path)
    print(f"PDF417 barcode saved successfully using treepoem as {file_path}")
except FileNotFoundError as e:
    print(f"Error: Could not find Ghostscript executable. Make sure Ghostscript is installed and in your PATH. Details: {e}")
except Exception as e:
    print(f"An error occurred: {e}")