from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Learn To Code at Codemy.com")
root.iconbitmap('TenochtitlanEscudo.ico')

my_img = ImageTk.PhotoImage(Image.open("images/TenochtitlanEscudo.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Quit', command=root.quit)
button_quit.pack()
# button_quit.grid(row=0, column=0, columnspan=3)


root.mainloop()

