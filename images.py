from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Learn To Code at Codemy.com")


my_img1 = ImageTk.PhotoImage(Image.open("images/Ollin.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/hummingbird.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/stonequetzalcoatl.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/reynadeflores.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/tlaloc.jpeg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(imagenum):
    global my_label
    global button_forward
    global button_back
    

    my_label.grid_forget()
    my_label = Label(image=image_list[imagenum-1])
    button_forward = Button(root, text='>>', command=lambda: forward(imagenum+1))
    button_back = Button(root, text='<<', command=lambda: back(imagenum-1))

    if imagenum == len(image_list):
        button_forward = Button(root, text='>>', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)




def back(imagenum):
    global my_label
    global button_forward
    global button_back
    

    my_label.grid_forget()
    my_label = Label(image=image_list[imagenum-1])
    button_forward = Button(root, text='>>', command=lambda: forward(imagenum+1))
    button_back = Button(root, text='<<', command=lambda: back(imagenum-1))

    if imagenum == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()

