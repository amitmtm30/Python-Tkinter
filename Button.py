from tkinter import *

root = Tk()
root.geometry("600x550")
# Creating label
label = Label(root, text="Hello Python")
label.pack()


# Creating callBack function
def callBack():
    label.config(text="You Clicked Me", fg='red', bg='Yellow')


# Creating button
button = Button(root, text="Click Me!")
button.pack()

# configuring the button, if you want to change the color when user click the button
button = Button(root, text="Click Me with changing option!", command=callBack)
button.pack()

root.mainloop()
