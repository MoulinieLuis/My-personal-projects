'''
In this Python program we will be exploring some concepts of Tkinter
a standard Python library used to program graphic interfaces
The library is already integrated, so there's o need to download anything
'''

import tkinter as tk

def show_message():
    name = name_entry.get()
    age = age_entry.get()
    message.config(text=f"Hello {name}, you are {age} years old!")
    
window = tk.Tk()
window.title("Name + Age")
window.geometry("500x500")

tk.Label(window, text="Enter your name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Enter your age:").pack()
age_entry = tk.Entry(window)
age_entry.pack()

message = tk.Label(window, text="", fg="blue")
message.pack()

tk.Button(window, text="Submit", command=show_message).pack()

window.mainloop()