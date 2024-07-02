import string
from tkinter import *
import tkinter as tk

window = Tk()
window.title("Password Strength Checker")
window.geometry("500x400")
window.resizable(True, True)

def check_password():
    password = password_box.get()
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if wspace_count>=1:
        strength +=1
    if special_count>=1:
        strength +=1

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength ==3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"    

    lower_label = Label(window, text=f"{lower_count} lowercase characters")
    lower_label.pack()

    upper_label = Label(window, text=f"{upper_count} uppercase characters")
    upper_label.pack()

    num_label = Label(window, text=f"{num_count} numeric characters")
    num_label.pack()

    wspace_label = Label(window, text=f"{wspace_count} whitespace characters")
    wspace_label.pack()

    special_label = Label(window, text=f"{special_count} special characters")
    special_label.pack()

    strength_label = Label(window, text=f"Password Strength:{strength}")
    strength_label.pack(pady=20)

    remarks_label = Label(window, text=f"Hint: {remarks}")
    remarks_label.pack()

def clear_box():
    password_box.delete(0, END)
    window.

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

# def check_pwd():
#     password = getpass.getpass("Enter Password: ")
#     strength = 0
#     remarks = ''
#     lower_count = upper_count = num_count = wspace_count = special_count = 0

#     for char in list(password):
#         if char in string.ascii_lowercase:
#             lower_count += 1
#         elif char in string.ascii_uppercase:
#             upper_count +=1
#         elif char in string.digits:
#             num_count += 1
#         elif char == ' ':
#             wspace_count +=1
#         else:
#             special_count +=1

#     if lower_count >= 1:
#         strength +=1
#     if upper_count >= 1:
#         strength +=1
#     if num_count >= 1:
#         strength +=1
#     if wspace_count>=1:
#         strength +=1
#     if special_count>=1:
#         strength +=1

#     if strength == 1:
#         remarks = "Very Bad Password!!! Change ASAP"
#     elif strength == 2:
#         remarks = "Not A Good Password!!! Change ASAP"
#     elif strength ==3:
#         remarks = "It's a weak password, consider changing"
#     elif strength == 4:
#         remarks = "It's a hard password, but can be better"
#     elif strength == 5:
#         remarks = "A very strong password"

#     print('Your password has: ')
#     print(f"{lower_count} lowercase characters")
#     print(f"{upper_count} uppercase characters")
#     print(f"{num_count} numeric characters")
#     print(f"{wspace_count} whitespace characters")
#     print(f"{special_count} special characters")

#     print(f"Password Strength:{strength}")
#     print(f"Hint: {remarks}")

# def ask_pwd(another_pwd=False):
#     valid = False
#     if another_pwd:
#         choice=input('Do you want to enter another pwd (y/n): ')
#     else:
#         choice=input('Do you want to check pwd (y/n): ')

#     while not valid:
#         if choice.lower() == 'y':
#             return True
#         elif choice.lower() == 'n':
#             return False
#         else:
#             print('Invalid, Try Again')
#             break

# if __name__ == '__main__':
#     print('+++ welcome to PWD checker +++')
#     ask_pw = ask_pwd()
#     while check_pwd:
#         check_pwd()
#         ask_pw = ask_pwd(True)