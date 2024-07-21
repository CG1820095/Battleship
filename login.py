
#password check
"""
(for the signup page - for version 1) test to check that if that if the password entered matches the comfirm password entered that the password validation will work
"""

from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3
import re 

root = Tk()
root.title("Create password")

root.configure(background="Light blue")

#prevents NameError: name 'message_label'
message_label = None

connection = sqlite3.connect('passwords.db')
cursor = connection.cursor()

cursor.execute("create table if not exists account_details(username text, userpassword text)")

#def resetusern(): 
#    cursor.execute("UPDATE account_details SET player1_ships = NULL")
#    cursor.execute("DELETE FROM board_details WHERE player1_ships IS NULL AND player2_ships IS NULL")
#    connection.commit()
#    messagebox.showinfo("PLAYER 1 BOARD", "SHIP SELECTION RESET")
#    print("killing board1")
#    root.destroy()
#    subprocess.run(["python", ("third.py")])

#reset_usern = Button(root, text="clear username", padx = 10, pady = 5, fg="orange", bg="black", activebackground="orange", activeforeground="black",command = p1resetplace)
#reset_usern.grid()


def create_account():
    global message_label
    # Get password
    password = Entry_password.get()
    confirm_password = Entry_confirmpassword.get()


    for row in cursor.execute("select * from account_details"): print(row)
    connection.commit()

      # Hide the existing message_label if it's present
    if message_label:
        message_label.grid_forget()

    if len(password) < 8 or len(password) > 20:
        message_label = ttk.Label(root, text="Password must be between 8 and 20 characters.", foreground="red",
                                  background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        message_label = ttk.Label(root, text="Password must contain at least one\n uppercase letter and one number.",
                                  foreground="red", background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    elif password != confirm_password:
            # Check if the passwords match
            message_label = ttk.Label(root, text="Passwords don't match.", foreground="red",
                                    background="Light blue", font=('Arial', 12, 'bold'))
            message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
    
    else: #if the password meets all the requirements then it can be saved to the database
        print(password)

        save = cursor.execute("INSERT INTO account_details(userpassword) VALUES(?)")
        connection.execute(save, (password,))


        for row in cursor.execute("select * from account_details "): print(row)
        connection.commit()

        #sql = "INSERT INTO TABLE (COLUMN) VALUES (?)"
        #conn.execute(sql, (user_input,))

Label_signup = ttk.Label(root, text="Sign up", font=("Arial", 20, "bold"), background="Light Blue")
Label_signup.grid(row=1, column=0, pady=30, padx=100)

Label_password = ttk.Label(root, text="Password", font=("Arial", 12, "bold"), background="Light Blue")
Label_password.grid(row=4, column=0, pady=0, padx=100)

Entry_password = ttk.Entry(root, show="*")
Entry_password.grid(row=5, column=0, pady=0, padx=100)

Label_confirmpassword = ttk.Label(root, text="Confirm Password", font=("Arial", 10,), background="Light Blue")
Label_confirmpassword.grid(row=6, column=0, pady=(20,0), padx=100)

Entry_confirmpassword = ttk.Entry(root, show="*")
Entry_confirmpassword.grid(row=7, column=0, padx=100)

#create account
Button = ttk.Button(root, text="Create Account", command=create_account)  
Button.grid(row=9, column=0, pady=(25,0), padx=100)

root.mainloop()