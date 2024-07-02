import string
from tkinter import *
import tkinter as tk

window = Tk()
window.title("Password Strength Checker")
window.geometry("500x400")
window.resizable(True, True)

def check_password():
    global lower_label, upper_label, num_label, special_label, strength_label, remarks_label

    password = password_box.get()
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        else:
            special_count +=1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if special_count>=1:
        strength +=1

    if strength == 0:
        remarks = "Please enter a valid password"
    elif strength == 1:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength ==2:
        remarks = "It's a weak password, consider changing"
    elif strength == 3:
        remarks = "It's a hard password, but can be better"
    elif strength == 4:
        remarks = "A very strong password"    

    lower_label = Label(window, text=f"{lower_count} lowercase characters")
    lower_label.pack()

    upper_label = Label(window, text=f"{upper_count} uppercase characters")
    upper_label.pack()

    num_label = Label(window, text=f"{num_count} numeric characters")
    num_label.pack()

    special_label = Label(window, text=f"{special_count} special characters")
    special_label.pack()

    strength_label = Label(window, text=f"Password Strength: {strength}")
    strength_label.pack(pady=20)

    remarks_label = Label(window, text=f"Hint: {remarks}")
    remarks_label.pack()

    check_button['state'] = DISABLED

def clear_box():
    password_box.delete(0, END)
    lower_label.destroy()
    upper_label.destroy()
    num_label.destroy()
    special_label.destroy()
    strength_label.destroy()
    remarks_label.destroy()

    check_button['state'] = NORMAL

lf = LabelFrame(window, text="Enter the password: ")
lf.pack(pady=20)

password_box = Entry(lf, font=("Poppins, 12"), width=25, justify=CENTER, show="*")
password_box.pack(padx=30, pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

check_button = Button(button_frame, text="Check Password", command=check_password)
check_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear Password", command=clear_box)
clear_button.grid(row=0, column=1, padx=10)

window.mainloop()