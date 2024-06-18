from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def calculate():
    km = round(1.609344*float(entry.get()), 2)
    label_4.config(text=f"{km}")


# Labels
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)


# Entry
entry = Entry(width=5)
entry.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)





window.mainloop()
