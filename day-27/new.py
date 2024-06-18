from tkinter import *

def button_clicked():
    print("Do something")

#Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
#Labels
my_label = Label(text="This is old text", font=("Aral", 24, "bold"))
my_label.config(text="This is new text")
my_label.grid(column=0, row=0)

#Buttons
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


#Entries
entry = Entry(width=30)
#Gets text in entry
print(entry.get())
entry.grid(column=3, row=2)

new_button = Button(text="Click Me Again", command=button_clicked)
new_button.grid(column=2, row=0)


window.mainloop()