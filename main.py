from tkinter import *
from tkinter import messagebox
from random import *
from PIL import Image, ImageTk



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)
    # Copy to clipboard using tkinter
    window.clipboard_clear()
    window.clipboard_append(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    email_id = email_entry.get()
    password = password_entry.get()

    if website_name == "" or email_id == "" or password == "":
        messagebox.showerror(title="Error", message="Please enter all the details!")
    else:
        response = messagebox.askquestion(title="Confirmation",
                                          message=f"Website : {website_name}\nEmail ID : {email_id}\nPassword : {password}\n\nIs this OK?")

        if response == "yes":
            messagebox.showinfo(title="Info", message="Data Saved Successfully")
            with open(file="password_information.txt", mode="a") as file:
                file.write(f"{website_name} | {email_id} | {password}\n")
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Lock Vault")
window.config(width=500, height=500)
window.config(padx=50, pady=50)

# CANVAS AND LOGO PIC
original_logo = Image.open("images/logo-transparent.png")
resized_logo = original_logo.resize((200, 200))
logo = ImageTk.PhotoImage(resized_logo)
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# WEBSITE LABEL
website_label = Label(text="Website:", font=("Arial", 15))
website_label.grid(row=1, column=0)

# WEBSITE ENTRY
website_entry = Entry(font=("Arial", 15), justify="center")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.config(width=35)
website_entry.focus()

# EMAIL/USERNAME LABEL
email_label = Label(text="Email/Username:", font=("Arial", 15))
email_label.grid(row=2, column=0)

# EMAIL/USERNAME ENTRY
email_entry = Entry(font=("Arial", 15), justify="center")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.config(width=35)

# PASSWORD LABEL
password_label = Label(text="Password:", font=("Arial", 15))
password_label.grid(row=3, column=0)

# PASSWORD ENTRY
password_entry = Entry(font=("Arial", 15), justify="center")
password_entry.grid(row=3, column=1)
password_entry.config(width=21)

# GENERATE PASSWORD BUTTON
generate_button = Button(text="Generate Password", command=generate_password, font=("Arial", 11))
generate_button.grid(row=3, column=2)

# ADD BUTTON
add_button = Button(text="Add", command=save_password, font=("Arial", 13))
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(width=42)

window.mainloop()
