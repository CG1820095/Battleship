from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess

root = Tk()
root.title("Battleships Account Login  ((Admin) (123))")
root.configure(background="light blue")
root.geometry("400x400")

root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open("Battleship\images\b4b440dc84c8a3e2922f502f54a01764.jpg")))

print("entered login page")


def Ok():
     uname = e1.get()
     password = e2.get()
       
     if(uname == "" and password == "") :
           messagebox.showinfo("", "Blank Not allowed")
       
       
     elif(uname == "Admin" and password == "123"):        
           messagebox.showinfo("","Login Success")
           root.destroy()
           subprocess.run(["python", r"BattleshipGaming\third.py"])
       
     else :
           messagebox.showinfo("","Incorrent Username and Password")

global e1
global e2
       
Label(root, text="UserName", background="grey").place(x=10, y=10)
Label(root, text="Password", background="grey").place(x=10, y=40)
       
e1 = Entry(root)
e1.place(x=140, y=10)
       
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
       
       
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)
       

def landing():
    print("killing login first")
    root.destroy()
    subprocess.run(["python", (r"BattleshipGaming\first.py")])

return_here = Button(root, text="Return", height = 3, width = 13, fg="black", bg="light blue", command = landing).place(x=270, y=100)

button_exit = Button(root, text="Exit Program", bg="yellow", command=root.quit).place(x=160, y=200)


root.mainloop()