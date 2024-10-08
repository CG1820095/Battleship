"""import tkinter for the gui functions"""
from tkinter import Tk, Label, Canvas, Button
import subprocess
from PIL import ImageTk, Image

root = Tk()
root.title("Battleships")


#icon for the game
root.tk.call('wm', 'iconphoto', root, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.configure(background="light blue")

welcome = Label(root, text="Welcome to", pady=0, padx=40, font=("Comic Sans MS", 10), bg="grey")
welcome.pack()
myLabel = Label(root, text="BATTLESHIPS", pady=0, padx=10, font=("Arial", 35, 'bold'), bg="grey")
myLabel.pack()

c = Canvas(root, width=600, height=275, background="grey")
c.pack()


#destroys the page then runs the next one with subprocess
def login():
    """Function to go to login page"""
    print("killing landing first")
    root.destroy()
    subprocess.run(["python", ("login.py")], check=False)

login_here = Button(root, text="LOGIN", padx = 10, pady = 5,
                    fg="black", bg="light blue", command = login)
login_here.pack()

#the user game go from the landing page to the signup page
def signup():
    """Function to go to signup page"""
    print("killing landing first")
    root.destroy()
    subprocess.run(["python", ("signup.py")], check=False)

signup_here = Button(root, text="SIGN UP", padx = 10, pady = 5, bg="light blue", command = signup)
signup_here.pack()


my_img = ImageTk.PhotoImage(Image.open ("images/battleship.jpg"))
c.create_image(300, 120,image = my_img, )

button_exit = Button(root, text="Exit Program", bg="yellow", command=root.quit)
button_exit.pack()

root.mainloop()
