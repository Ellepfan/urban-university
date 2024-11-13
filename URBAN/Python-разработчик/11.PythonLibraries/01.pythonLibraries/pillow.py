from PIL import Image
from PIL import ImageFilter

# Pillow и его предшественник PIL — это оригинальные библиотеки Python для работы с изображениями.


image = Image.open('1.jpeg')
rotated = image.rotate(180)
rotated.save('./1_1.jpeg')




image = Image.open('1.jpeg')
blurred_jelly = image.filter(ImageFilter.BLUR)
blurred_jelly.save('./1_2.jpeg')
blurred_jelly = image.filter(ImageFilter.SHARPEN)
blurred_jelly.save('./1_2.jpeg')


image.save('./1_3.png', 'png')



grayscale = image.convert('L')
grayscale.save('./1_4.jpeg')