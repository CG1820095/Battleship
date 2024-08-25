from tkinter import *
from tkinter import ttk, messagebox
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk

root = Tk()
root.title("Create Account")

root.tk.call('wm', 'iconphoto', root, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.configure(background="Light blue")

#prevents NameError: name 'MESSAGE_LABEL'
MESSAGE_LABEL = None

#connecting to the database
connection = sqlite3.connect('battleships.db')
cursor = connection.cursor()

cursor.execute("create table if not exists account_details(username text, userpassword text)")


def create_account():
    """Function to create a username and password"""
    global MESSAGE_LABEL
    # Get password
    password = Entry_password.get()
    confirm_password = Entry_confirmpassword.get()
    username = Entry_username.get()

      # Hide the existing MESSAGE_LABEL if it's present
    if MESSAGE_LABEL:
        MESSAGE_LABEL.grid_forget()

    if len(password) < 8 or len(password) > 20:
        MESSAGE_LABEL = ttk.Label(root, text="Password must be between 8 and 20 characters.",
                                  foreground="red",background="Light blue",font=('Arial',12,'bold'))
        MESSAGE_LABEL.grid(row=14, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        MESSAGE_LABEL=ttk.Label(root,
                                text="must contain at least one\n uppercase letter and one number",
                                foreground="red", background="Light blue",font=('Arial',12,'bold'))
        MESSAGE_LABEL.grid(row=14, column=0, padx=10, pady=5, columnspan=2)
        return

    elif password != confirm_password:
            # Check if the passwords match
        MESSAGE_LABEL = ttk.Label(root, text="Passwords don't match.", foreground="red",
                                    background="Light blue", font=('Arial', 12, 'bold'))
        MESSAGE_LABEL.grid(row=14, column=0, padx=10, pady=5, columnspan=2)

    else: #if password meets all requirements it can be saved to the database, and start the game
        cursor.execute("INSERT INTO account_details(userpassword,username) VALUES('{}', '{}')"
                       .format(password, username))
        connection.commit()
        messagebox.showinfo("BATTLESHIPS", "Signup complete")
        root.destroy()
        subprocess.run(["python", ("third.py")], check=False)


#lables and inputs for the users
Label_signup = ttk.Label(root, text="Sign up", font=("Arial", 20, "bold"), background="Light Blue")
Label_signup.grid(row=1, column=0, pady=30, padx=100)

Label_username = ttk.Label(root, text="Username", font=("Arial",12,"bold"), background="Light Blue")
Label_username.grid(row=3, column=0, pady=0, padx=100)

Entry_username = ttk.Entry(root,)
Entry_username.grid(row=4, column=0, pady=0, padx=100)

Label_password = ttk.Label(root, text="Password", font=("Arial",12,"bold"), background="Light Blue")
Label_password.grid(row=6, column=0, pady=(20,0), padx=100)

Entry_password = ttk.Entry(root, show="*")
Entry_password.grid(row=7, column=0, pady=0, padx=100)

Label_confirmpassword = ttk.Label(root, text="Confirm Password",
                                  font=("Arial", 10,), background="Light Blue")
Label_confirmpassword.grid(row=8, column=0, pady=(20,0), padx=100)

Entry_confirmpassword = ttk.Entry(root, show="*")
Entry_confirmpassword.grid(row=9, column=0, padx=100)

#create account
Button = ttk.Button(root, text="Create Account", command=create_account)
Button.grid(row=10, column=0, pady=(25,0), padx=100)

#return to previous page, landing page
def landing():
    """Function to return to landing page"""
    root.destroy()
    messagebox.showinfo("BATTLESHIPS", "returning to landing page")
    subprocess.run(["python", ("first.py")], check=False)

Button = ttk.Button(root, text="return", command=landing)
Button.grid(row=11, column=0, pady=(25,0), padx=100)

root.mainloop()
