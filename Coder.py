import tkinter.filedialog as fd

text = input()

filetypes = (("Текстовый файл", "*.txt"),
             ("Изображение", "*.jpg *.gif *.png"),
             ("Любой", "*"))
filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
if filename:
    print(filename)
