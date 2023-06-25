from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# 3 things image link, json contents, image font.


response = requests.get("https://i.imgur.com/egjySwy.png")

names = ['Chilumala Indira', 'Vinjamuri Navya Sri', 'Kandukuri Venkat Ganesh', 'Vallala Jeevana Sri',
         'Nallapu Raj Kumar', 'G Soumya', 'Jinkala Naveen Kumar', 'K Sangeeta', 'A Subramanyam Swamy', 'Pothula Ashwitha Reddy']
for name in names:
    # Open the image file
    # image_data = BytesIO(response.content)

    image = Image.open("ieee.png")

    X, Y = (image.size)
    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Define the font size and type
    # font = ImageFont.truetype("Agrandir-TextBold.ttf", 50)
    font = ImageFont.truetype("DMSerifDisplay-Regular.ttf", 60)

    # Define the text to be added

    # Define the x and y position for the text
    x, y = X // 2 - 300, Y // 2
    print(x, y, X, Y)

    w, h = draw.textsize(name, font=font)
    print(w, h)
    draw.text((((X - w) / 2), ((Y - h) / 2)),
              name, fill=(255, 255, 255), font=font)

    # Save the image as a PNG file with no quality loss
    file_name = f"{name} - IEEE Certificate.pdf"
    image.save(f"IEEE Certs/{file_name}", optimize=True, quality=100)
