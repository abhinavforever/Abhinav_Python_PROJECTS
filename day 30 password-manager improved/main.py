from tkinter import messagebox
import random
import pyperclip
import json
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
    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    password=''.join(password_list)
    e3.insert(0,password)

    pyperclip.copy(e3.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=e1.get()
    email=e2.get()
    password=e3.get()
    new_data={
        website:{
        "email":email,
        "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showerror("OOPS!","Do not leave any fields as empty")
    else:
        try:
            with open("data.json","r") as f:
                # #Reading the old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(new_data, f, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json","w") as f:
                #Saving updated data
                json.dump(data,f,indent=4)
        finally:
            e1.delete(0,END)
            e3.delete(0,END)
# ---------------------------- Password finder ------------------------------- #
def find_password():
    website = e1.get()
    try:
        with open("data.json","r") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Oops",message="No Data File Found")
    else:
        try:
            messagebox.showinfo(title=website,message=f"email:{data[website]['email']}\npassword: {data[website]['password']}")
        except KeyError:
            messagebox.showerror(title='Oops',message="Data not found")

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

search=Button(text="Search",justify=CENTER,highlightthickness=0,command=find_password)
search.grid(row=1,column=2)

window.mainloop()

