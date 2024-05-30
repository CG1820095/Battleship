from tkinter import *
from PIL import ImageTk, Image
import subprocess
#from pytube import YouTube

root = Tk()
root.title("Battleships")
root.configure(background="light blue")
#root.geometry("690x690")

root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open("Battleship\images\icon.png")))


welcome = Label(root, text="Welcome to", pady=0, padx=40, font=("Comic Sans MS", 10), background="grey")
welcome.pack()
myLabel = Label(root, text="BATTLESHIPS", pady=0, padx=10, font=("Arial", 35, 'bold'), background="grey")
myLabel.pack()


c = Canvas(root, width=600, height=275, background="grey")
c.pack()


def login():
    print("killing landing first")
    root.destroy()
    subprocess.run(["python", ("Battleship/second.py")])


login_here = Button(root, text="LOGIN", padx = 10, pady = 5, fg="black", bg="light blue", command = login)
login_here.pack()


#my_img = ImageTk.PhotoImage(Image.open ("Battleship\images\battleship.jpg"))
#c.create_image(300, 120,image=my_img, )

button_exit = Button(root, text="Exit Program", bg="yellow", command=root.quit)
button_exit.pack()



#try:
#    url = input("Enter the YouTbue URL: ")

#    yt = YouTube(url)

#    print("Title: ", yt.title)
#    print("Views:", yt.views)

#    yd = yt.streams.get_highest_resolution()

#    yd.download()

#    print("Download complete. ")
#except Exception as e:
#    print("An error occurred: ", str(e))


root.mainloop()