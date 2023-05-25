from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_password():
    website = website_entry.get()
    with open("password manager/data.json", "r") as data_file:
            data = json.load(data_file)
            try:
                username = data[f"{website}"]["email"]
                password = data[f"{website}"]["password"]
            except KeyError:
                messagebox.showinfo(title="Oops", message=f"No Information Exists")
            else:
                messagebox.showinfo(title="Oops", message=f"This website exists\n Username: {username}\n Password: {password}")
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
""
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("password manager/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("password manager/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    
    
    


# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

#image
canvas = Canvas(width=200,height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="password manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
#website label
website_label = Label(text="Website:",bg="white",fg="black")
website_label.grid(row=1,column=0)
#email/username label
username_label = Label(text="Email/Username:",bg="white",fg="black")
username_label.grid(row=2,column=0)
#password label
password_label = Label(text="Password:",bg="white",fg="black")
password_label.grid(row=3,column=0)
#website entry
website_entry = Entry(width=21,bg="white",highlightthickness=0,fg="black")
website_entry.grid(row=1,column=1)
website_entry.focus()
#email/username entry
username_entry = Entry(width=36,bg="white",highlightthickness=0,fg="black")
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0, "eligrimaldi@berkeley.edu")
#password entry
password_entry = Entry(width=21,bg="white",highlightthickness=0,fg="black")
password_entry.grid(row=3,column=1)
#generate password button
password_button = Button(width=14,text="Generate Password", highlightthickness = 0,highlightbackground="white", command=generate_password)
password_button.grid(row=3,column=2)
#add button
add_button = Button(width=36,text="Add", highlightbackground='white',command=save_info)
add_button.grid(row=4,column=1,columnspan=2)
search_button = Button(width=14,text="Search", highlightbackground='white',command=search_password)
search_button.grid(row=1,column=2)
window.mainloop()