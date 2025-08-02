from PIL import Image

img = Image.new('RGB',
                (200, 100),
                color='black')

img.save("image.png")