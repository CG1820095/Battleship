from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
import sqlite3
import re 
from tkinter import messagebox 

root = Tk()
root.title("Login with an existing Account")

#root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open("images/temp.png")))


root.configure(background="light blue")

#prevents NameError: name 'message_label'
message_label = None

connection = sqlite3.connect('battleships.db', timeout=120.0)
cursor = connection.cursor()

def login_account():
    global message_label
    # Get password
    password = Entry_password.get()
    username = Entry_username.get()

      # Hide the existing message_label if it's present
    if message_label:
        message_label.grid_forget()

    if len(password) < 8 or len(password) > 20:
        message_label = ttk.Label(root, text="If you do not have an existing account please sign up", foreground="red",
                                  background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=14, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        message_label = ttk.Label(root, text="If you do not have an existing account please sign up",
                                  foreground="red", background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=14, column=0, padx=10, pady=5, columnspan=2)
        return
    
    else: #if the password meets all the requirements then check if its saved to the database
        cursor.execute("SELECT * FROM account_details WHERE username = '{}' and userpassword = '{}'".format(username, password))
        connection.commit()
        connection.close()
        messagebox.showinfo("BATTLESHIPS", "Login success")
        root.destroy()
        subprocess.run(["python", ("third.py")])
        


Label_login = ttk.Label(root, text="Login", font=("Arial", 20, "bold"), background="Light Blue")
Label_login.grid(row=1, column=0, pady=30, padx=100)

Label_username = ttk.Label(root, text="Username", font=("Arial", 12, "bold"), background="Light Blue")
Label_username.grid(row=3, column=0, pady=0, padx=100)

Entry_username = ttk.Entry(root,)
Entry_username.grid(row=4, column=0, pady=0, padx=100)

Label_password = ttk.Label(root, text="Password", font=("Arial", 12, "bold"), background="Light Blue")
Label_password.grid(row=6, column=0, pady=(20,0), padx=100)

Entry_password = ttk.Entry(root, show="*")
Entry_password.grid(row=7, column=0, pady=0, padx=100)

#login to account
Button = ttk.Button(root, text="login", command=login_account)  
Button.grid(row=10, column=0, pady=(25,0), padx=100)


def landing():
    root.destroy()
    messagebox.showinfo("BATTLESHIPS", "returning to landing page")
    subprocess.run(["python", ("first.py")])
    
Button = ttk.Button(root, text="return", command=landing)  
Button.grid(row=11, column=0, pady=(25,0), padx=100)


root.mainloop()