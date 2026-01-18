from PIL import Image

im = Image.open("images/kisa.jpg")
print(f'image size {im.size}')

# box = (0, 0, 1000, 1000)
# region = im.crop(box)
# region.show()

# ВНИМАНИЕ! В Pillow первой координатой идет X!
for x in range(im.size[0] // 2):
    for y in range(im.size[1] // 2):
        pix = im.getpixel((x, y))
        avg = (pix[0] + pix[1] + pix[2]) //3
        im.putpixel((x, y), (avg, avg, avg))

im.show()
im.save('./kisa.jpg')