from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v'
        , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S'
        , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # pass_key = ""
    # for char in password_list:
    #     pass_key += char
    pass_key = "".join(password_list)
    password_entry.insert(0, pass_key)
    pyperclip.copy(pass_key)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get().capitalize()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if (len(website) or len(password)) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
        #                                                           f"\nPassword: {password}\nIs it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH DATA ------------------------------- #


def find_password():
    website = web_entry.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    if website in data:
        messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                   f"Password: {data[website]['password']}")
    else:
        messagebox.showinfo(title="Websit not Found", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas
canvas = Canvas(height=200, width=200)
my_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_logo)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pas_label = Label(text="Password:")
pas_label.grid(column=0, row=3)

# Buttons
generate = Button(text="Generate Password", width=15, command=generate_password)
generate.grid(column=2, row=3, sticky="w")

add = Button(text="Add", width=44, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)

# Entries
web_entry = Entry(width=33)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "stathovits@hotmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, columnspan=1)

window.mainloop()
