from PIL import Image,ImageFont, ImageDraw


my_image = Image.open("images/sample.jpeg")

title_font = ImageFont.truetype('fonts/font.ttf', 100)
title_text = "Sample Text"
image_editable = ImageDraw.Draw(my_image)

image_editable.text((375,100), title_text, (0, 0, 0), font=title_font)
my_image.save("result.jpg")



