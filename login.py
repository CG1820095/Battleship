"""import tkinter for the gui"""
from tkinter import Tk, ttk, messagebox
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk

root = Tk()
root.title("Login with an existing Account")

root.tk.call('wm', 'iconphoto', root, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.configure(background="light blue")

#prevents NameError: name 'MESSAGE_LABEL'
MESSAGE_LABEL = None

connection = sqlite3.connect('battleships.db')
cursor = connection.cursor()

def login_account():
    """Function to sign in with an existing username and password"""
    global MESSAGE_LABEL
    # Get password
    password = Entry_password.get()
    username = Entry_username.get()

      # Hide the existing MESSAGE_LABEL if it's present
    if MESSAGE_LABEL:
        MESSAGE_LABEL.grid_forget()

    if len(password) < 8 or len(password) > 20:
        MESSAGE_LABEL=ttk.Label(root, text="If you do not have an existing account please sign up",
                                foreground="red",background="Light blue",font=('Arial',12,'bold'))
        MESSAGE_LABEL.grid(row=14, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        MESSAGE_LABEL=ttk.Label(root, text="If you do not have an existing account please sign up",
                                foreground="red",background="Light blue",font=('Arial',12,'bold'))
        MESSAGE_LABEL.grid(row=14, column=0, padx=10, pady=5, columnspan=2)
        return

    else: #if the password meets all the requirements then check if its saved to the database
        for row in cursor.execute("""SELECT EXISTS(SELECT * FROM account_details WHERE
                                  username = '{}' and userpassword = '{}')""".format(username, password)):

            if row == (0,): #if row returns false, provide error message
                MESSAGE_LABEL=ttk.Label(root,
                                        text="If you don't have an existing account please sign up",
                                        foreground="red",background="Light blue",
                                        font=('Arial',12,'bold'))
                MESSAGE_LABEL.grid(row=14, column=0, padx=10, pady=5, columnspan=2)

            if row == (1,): #if row returns true, start the game
                messagebox.showinfo("BATTLESHIPS", "Login success")
                root.destroy()
                subprocess.run(["python", ("third.py")], check=False)

        connection.commit()


Label_login = ttk.Label(root, text="Login", font=("Arial",20,"bold"), background="Light Blue")
Label_login.grid(row=1, column=0, pady=30, padx=100)

Label_username = ttk.Label(root, text="Username", font=("Arial",12,"bold"), background="Light Blue")
Label_username.grid(row=3, column=0, pady=0, padx=100)

Entry_username = ttk.Entry(root,)
Entry_username.grid(row=4, column=0, pady=0, padx=100)

Label_password = ttk.Label(root, text="Password", font=("Arial",12,"bold"), background="Light Blue")
Label_password.grid(row=6, column=0, pady=(20,0), padx=100)

Entry_password = ttk.Entry(root, show="*")
Entry_password.grid(row=7, column=0, pady=0, padx=100)

#login to account
Button = ttk.Button(root, text="login", command=login_account)
Button.grid(row=10, column=0, pady=(25,0), padx=100)


def landing():
    """Function to return to landing page"""
    root.destroy()
    messagebox.showinfo("BATTLESHIPS", "returning to landing page")
    subprocess.run(["python", ("first.py")], check=False)

Button = ttk.Button(root, text="return", command=landing)
Button.grid(row=11, column=0, pady=(25,0), padx=100)


root.mainloop()
