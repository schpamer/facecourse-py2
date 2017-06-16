from PIL import Image

img = Image.open("/home/mullet/Pictures/F-16_June_2008.jpg")
print(img.size)
print(img.format)

img.show()