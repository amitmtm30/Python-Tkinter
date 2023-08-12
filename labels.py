from tkinter import *

# Creating a root windows
root = Tk()

# Adjusting root windows size
root.geometry("500x450")

# Creating a label
label = Label(root, text="Hello Python")
# configuring the label
label['text'] = "Changing text using dict"
label.config(text="Hello Tkinter")

# configuring the text format
label.config(font='Calibre 15')

# configuring the long text
label.config(text="Hello Python I love you very much")

# configuring to wrap the long text in to 200 pixel
label.config(wraplength='200')

# configuring the text color
label.config(fg='red')

# configure the default alignment to right alignment
label.config(justify=RIGHT)

# configuring the text background color
label.config(background='yellow')
label.pack()

# run the windows
root.mainloop()
