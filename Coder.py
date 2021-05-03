import tkinter.filedialog as fd
from PIL import Image


code = []
print('Что вы хотите сделать?')
print('1 - Закодировать текст в изображение (нужно будет выбрать .txt файл)')
print('2 - Прочитать текст из изображения (нужно будет выбрать .jpg/.png файл)')
choice = input('(1 / 2) : ')

filename = fd.askopenfilename(title="Открыть файл")
if filename:
    if '.jpg' in filename or '.png' in filename:
        image = Image.open(filename)
        for i in range(image.width):
            for j in range(image.height):
                pixel = image.getpixel((i, j))
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                    code.append('0')
                elif pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 255:
                    code.append('1')
                elif pixel[0] == 0 and pixel[1] == 255 and pixel[2] == 0:
                    code.append('2')
                elif pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 0:
                    code.append('3')
                elif pixel[0] == 0 and pixel[1] == 255 and pixel[2] == 255:
                    code.append('4')
                elif pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 0:
                    code.append('5')
                elif pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 255:
                    code.append('6')
                elif pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                    code.append('7')
    elif '.txt' in filename:
        text = open(filename, 'r')
        print(*text.read())
print(*code)
