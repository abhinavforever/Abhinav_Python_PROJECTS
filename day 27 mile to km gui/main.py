from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

input=Entry(width=15,highlightbackground="blue",highlightthickness=2)
input.grid(column=1,row=0)

label1=Label(text="Miles",font=("Arial", 14, "bold"))
label1.grid(column=2,row=0)

label2=Label(text="is equal to",font=("Arial", 14, "bold"))
label2.grid(column=0,row=1)


text=Text(height=1,width=15)
text.grid(column=1,row=1)

label3=Label(text="km",font=("Arial", 14, "bold"))
label3.grid(column=2,row=1)

# 1 mile = 1.60934 km
def button_clicked():
    text.delete("1.0","end")
    text.insert('1.0',str(int(input.get()) * 1.60934))

button=Button(text="Calculate",font=("Aria",14,"bold"),command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()
