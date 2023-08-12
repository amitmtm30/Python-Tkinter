from tkinter import *
from tkinter import ttk


# Creating root windows
root = Tk()

# creating the root windows dimension
root.geometry("400x350")
# Creating windows using tkinter
button1 = Button(root, text='Click Me!')
button1.pack()
# Creating Button using ttk
button2 = ttk.Button(root, text='Click Me!')
button2.pack()
# Run the application
root.mainloop()