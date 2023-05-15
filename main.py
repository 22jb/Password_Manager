from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def gen_password():
    password_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [ random.choice(letters) for char in range(nr_letters)]
    password_symbols = [ random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [ random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    #print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_input():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    #messagebox.showinfo(title="Title", message="Message")
    if username == "" or password == "":
        messagebox.showerror(message="Please ensure no fields are empty")
    else:
        # user_answer = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
        #                                                 f"\nPassword: {password} \nIs it ok to save?")
        #
        # if user_answer is True:
        try:
            with open("password_manager.json", "r") as file:
                #file.write(f"{website} | {username} | {password}\n")

                #json.dump(new_data, file, indent=4
                data = json.load(file)
        except FileNotFoundError:
            with open("password_manager.json", "w") as file:

                #data.update(new_data)
                json.dump(new_data, file, indent=4)
        else:

                data.update(new_data)
                with open("password_manager.json", "w") as file:
                    json.dump(data, file, indent=4)
            #print(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- Search Function------------------------- #

def search():
    target_key = website_entry.get()
    try:
        with open("password_manager.json", "r") as file:
            json_data = json.load(file)


    except FileNotFoundError:
        messagebox.showerror(title="File Empty", message="No value in file please add a password")
    # except target_key == "":
    #     messagebox.showerror(title="No website entered", message="Please ensure website entry box is not empty")

    else:
        if target_key in json_data:
            email = json_data.get(target_key).get("email")
            password = json_data.get(target_key).get("password")
            messagebox.showinfo(title=f"{target_key}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Key not found", message="Website could not be found")
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(column=1, row=0)


# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1,columnspan=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, columnspan=1)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, columnspan=1)

#Entries

website_entry = Entry(width=35)
website_entry.grid(sticky=W,column=1, row=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(sticky=W,column=1, row=2,columnspan=2)
email_entry.insert(index=END, string="joseph.brown@yahoo.com")

password_entry = Entry(width=35)
password_entry.grid(sticky=W,column=1, row=3,columnspan=2)

# Buttons

generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(sticky=W,column=2, row=3, columnspan=1)

add_button = Button(text="Add",width=43, command=add_input)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(width=15,text="Search", command=search)
search_button.grid(sticky=W,column=2, row=1, columnspan=1)

window.mainloop()

