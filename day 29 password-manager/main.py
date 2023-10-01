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

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list.extend([random.choice(letters) for _ in range(nr_letters)])

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password=''.join(password_list)

    # print(f"Your password is: {password}")
    e3.insert(0,password)

    pyperclip.copy(e3.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=e1.get()
    email=e2.get()
    password=e3.get()
    is_ok=False

    if len(website)==0 or len(password)==0:
        messagebox.showerror("OOPS!","Do not leave any fields as empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email} \nPassword: {password} "
                                                 f"\nIs it ok to Save?")
    if is_ok:
        with open("data.txt","a") as f:
            f.write(f"{website} | ")
            f.write(f"{email} | ")
            f.write(f"{password}\n")
            e1.delete(first=0,last=len(website))
            e3.delete(first=0, last=len(password))

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas( width=200, height=200,highlightthickness=0)
canvas.grid(row=0,column=1)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
#width of canvas is 200 and height is also 200,so the image should be placed at x=100,y=100 for it to be positioned at the centre

website_l=Label(text="Website:")
website_l.grid(column=0,row=1)
e1=Entry(width=35,highlightthickness=0)
e1.grid(row=1,column=1,columnspan=2)
e1.focus()

email_l=Label(text="Email/Username:")
email_l.grid(column=0,row=2)
e2=Entry(width=35,highlightthickness=0)
e2.grid(row=2,column=1,columnspan=2)
e2.insert(0,"abhinavsri204@gmail.com")

pass_l=Label(text="Password:")
pass_l.grid(row=3,column=0)
e3=Entry(width=21,highlightthickness=0)
e3.grid(row=3,column=1)

generate_pass=Button(text="Generate Password",highlightthickness=0,command=generate_password)
generate_pass.grid(row=3,column=2)
generate_pass.config(width=16)

add=Button(text="Add",justify=CENTER,highlightthickness=0,command=save)
add.grid(row=4,column=1,columnspan=2)
add.config(width=36)


window.mainloop()

