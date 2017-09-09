from tkinter import *

window = Tk()

def kgToGramPoundOunce():
    kg = float(kgEntryValue.get())
    gram  = str((kg * 1000)) + " gram"
    pound = str((kg * 2.20462)) + " pound"
    ounce = str((kg * 35.274)) + " ounce"

    gramText.insert(END, gram)
    poundText.insert(END, pound)
    ounceText.insert(END, ounce)


label = Label(text="Kg")
label.grid(row=0, column=0)

kgEntryValue = StringVar()
kgEntry = Entry(window, textvariable=kgEntryValue)
kgEntry.grid(row=0, column=1)

convertButton = Button(window, text="Convert", command=kgToGramPoundOunce)
convertButton.grid(row=0, column=2)

# gram text
gramText = Text(window, height=1, width=20)
gramText.grid(row=1, column=0)

# pund text
poundText = Text(window, height=1, width=20)
poundText.grid(row=1, column=1)

# ounce text
ounceText = Text(window, height=1, width=20)
ounceText.grid(row=1, column=2)

window.mainloop()
