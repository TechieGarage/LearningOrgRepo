from tkinter import *

# Creating main window
window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)


# Creating widgets
b1 = Button(window, text="Click", command=km_to_miles)
b1.grid(row=1, column=0)

# Entry widget is like text input in html
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

# Text widget is like textarea in html
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=1)

# Running the mainloop so that the GUI won't close quickly and stay opened.
window.mainloop()
