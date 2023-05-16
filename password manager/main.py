from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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
    with open("password manager/login_info.txt", "a") as file:
        username = username_entry.get()
        website = website_entry.get()
        password = password_entry.get()
        if not website or not password:
            messagebox.showerror(title="Error", message=f"Please don't leave any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered for {website}: \nEmail: {username}"
            f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

    
    
    


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
website_entry = Entry(width=35,bg="white",highlightthickness=0,fg="black")
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
#email/username entry
username_entry = Entry(width=35,bg="white",highlightthickness=0,fg="black")
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
window.mainloop()