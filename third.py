from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import sqlite3
from tkinter import messagebox 


root = Tk()
root.title("PLAYER 1 SHIP PLACEMENTS")

root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.geometry("900x600")
root.configure(background="light green")


connection = sqlite3.connect("battleships.db")
cursor = connection.cursor()

cursor.execute("create table if not exists board_details(player1_ships text, player2_ships text, player1_guess text, player2_guess text)")
connection.commit()

board1 = Frame(root, background="light green")
board1.place(relx=0.5, rely=0.5, anchor= CENTER,)


def gamequit():
    cursor.execute("DROP TABLE board_details")
    messagebox.showinfo("BATTLESHIPS", "killing game")
    root.quit()

button_exit = Button(board1, text="Exit Program", bg="yellow", activebackground="red", activeforeground="white", command = gamequit )
button_exit.grid(row=9, column=9)


def p1guessing():
    if p1shipcount < 17:
        messagebox.showinfo("!!!PLAYER 1!!!","CHOOSE ALL YOUR 17 SHIP SPACES BEFORE CONFIRMATION")

    else:
        messagebox.showinfo("PLAYER 1 CONFIRMED SHIP POSITIONS", "NOW PLAYER 2 PICKS THEIR SHIP LOCATIONS")
        print("killing board1")
        root.destroy()
        subprocess.run(["python", ("fourth.py")])



def p1resetplace(): 
    cursor.execute("UPDATE board_details SET player1_ships = NULL")
    connection.commit()
    cursor.execute("DELETE FROM board_details WHERE player1_ships IS NULL AND player2_ships IS NULL")
    connection.commit()
    messagebox.showinfo("PLAYER 1 BOARD", "SHIP SELECTION RESET")
    print("killing board1")
    root.destroy()
    subprocess.run(["python", ("third.py")])


p1_con_place = Button(root, text="CONFIRM SHIP PLACEMENT", padx = 10, pady = 5, fg="orange", bg="black", activebackground="orange", activeforeground="black", command = p1guessing)
p1_con_place.grid()

p1_res_place = Button(root, text="reset placement", padx = 10, pady = 5, fg="orange", bg="black", activebackground="orange", activeforeground="black",command = p1resetplace)
p1_res_place.grid()



#Define global ship count.
p1shipcount = 0

playerlabel = Label(text="PLAYER 1:", bg="light green")
playerlabel.grid(row=7, column=0)

#count display
countlabel = Button(root, text = "place ships of any size", bg="light green", activebackground="light yellow")
countlabel.grid(row = 9, column = 0, columnspan = 2,)

limitlabel = Label(text="(no more or less than 17 spaces)", bg="light green")
limitlabel.grid(row=10, column=0)

# Before first click
A1Clicked  = False 
A2Clicked  = False
A3Clicked  = False
A4Clicked  = False
A5Clicked  = False
A6Clicked  = False
A7Clicked  = False
A8Clicked  = False
A9Clicked  = False

B1Clicked  = False 
B2Clicked  = False
B3Clicked  = False
B4Clicked  = False
B5Clicked  = False
B6Clicked  = False
B7Clicked  = False
B8Clicked  = False
B9Clicked  = False

C1Clicked  = False 
C2Clicked  = False
C3Clicked  = False
C4Clicked  = False
C5Clicked  = False
C6Clicked  = False
C7Clicked  = False
C8Clicked  = False
C9Clicked  = False

D1Clicked  = False 
D2Clicked  = False
D3Clicked  = False
D4Clicked  = False
D5Clicked  = False
D6Clicked  = False
D7Clicked  = False
D8Clicked  = False
D9Clicked  = False

E1Clicked  = False 
E2Clicked  = False
E3Clicked  = False
E4Clicked  = False
E5Clicked  = False
E6Clicked  = False
E7Clicked  = False
E8Clicked  = False
E9Clicked  = False

F1Clicked  = False 
F2Clicked  = False
F3Clicked  = False
F4Clicked  = False
F5Clicked  = False
F6Clicked  = False
F7Clicked  = False
F8Clicked  = False
F9Clicked  = False

G1Clicked  = False 
G2Clicked  = False
G3Clicked  = False
G4Clicked  = False
G5Clicked  = False
G6Clicked  = False
G7Clicked  = False
G8Clicked  = False
G9Clicked  = False

H1Clicked  = False 
H2Clicked  = False
H3Clicked  = False
H4Clicked  = False
H5Clicked  = False
H6Clicked  = False
H7Clicked  = False
H8Clicked  = False
H9Clicked  = False

I1Clicked  = False 
I2Clicked  = False
I3Clicked  = False
I4Clicked  = False
I5Clicked  = False
I6Clicked  = False
I7Clicked  = False
I8Clicked  = False
I9Clicked  = False


def shiplimit():
    
    if A1Clicked == False:
        A1.configure(fg="black", bg="white", state=DISABLED)
    if A2Clicked == False:
        A2.configure(fg="black", bg="white", state=DISABLED)
    if A3Clicked == False:
        A3.configure(fg="black", bg="white", state=DISABLED)
    if A4Clicked == False:
        A4.configure(fg="black", bg="white", state=DISABLED)
    if A5Clicked == False:
        A5.configure(fg="black", bg="white", state=DISABLED)
    if A6Clicked == False:
        A6.configure(fg="black", bg="white", state=DISABLED)
    if A7Clicked == False:
        A7.configure(fg="black", bg="white", state=DISABLED)
    if A8Clicked == False:
        A8.configure(fg="black", bg="white", state=DISABLED)
    if A9Clicked == False:
        A9.configure(fg="black", bg="white", state=DISABLED)
    
    
    if B1Clicked == False:
        B1.configure(fg="black", bg="white", state=DISABLED)
    if B2Clicked == False:
        B2.configure(fg="black", bg="white", state=DISABLED)
    if B3Clicked == False:
        B3.configure(fg="black", bg="white", state=DISABLED)
    if B4Clicked == False:
        B4.configure(fg="black", bg="white", state=DISABLED)
    if B5Clicked == False:
        B5.configure(fg="black", bg="white", state=DISABLED)
    if B6Clicked == False:
        B6.configure(fg="black", bg="white", state=DISABLED)
    if B7Clicked == False:
        B7.configure(fg="black", bg="white", state=DISABLED)
    if B8Clicked == False:
        B8.configure(fg="black", bg="white", state=DISABLED)
    if B9Clicked == False:
        B9.configure(fg="black", bg="white", state=DISABLED)

    if C1Clicked == False:
        C1.configure(fg="black", bg="white", state=DISABLED)
    if C2Clicked == False:
        C2.configure(fg="black", bg="white", state=DISABLED)
    if C3Clicked == False:
        C3.configure(fg="black", bg="white", state=DISABLED)
    if C4Clicked == False:
        C4.configure(fg="black", bg="white", state=DISABLED)
    if C5Clicked == False:
        C5.configure(fg="black", bg="white", state=DISABLED)
    if C6Clicked == False:
        C6.configure(fg="black", bg="white", state=DISABLED)
    if C7Clicked == False:
        C7.configure(fg="black", bg="white", state=DISABLED)
    if C8Clicked == False:
        C8.configure(fg="black", bg="white", state=DISABLED)
    if C9Clicked == False:
        C9.configure(fg="black", bg="white", state=DISABLED)
        
    if D1Clicked == False:
        D1.configure(fg="black", bg="white", state=DISABLED)
    if D2Clicked == False:
        D2.configure(fg="black", bg="white", state=DISABLED)
    if D3Clicked == False:
        D3.configure(fg="black", bg="white", state=DISABLED)
    if D4Clicked == False:
        D4.configure(fg="black", bg="white", state=DISABLED)
    if D5Clicked == False:
        D5.configure(fg="black", bg="white", state=DISABLED)
    if D6Clicked == False:
        D6.configure(fg="black", bg="white", state=DISABLED)
    if D7Clicked == False:
        D7.configure(fg="black", bg="white", state=DISABLED)
    if D8Clicked == False:
        D8.configure(fg="black", bg="white", state=DISABLED)
    if D9Clicked == False:
        D9.configure(fg="black", bg="white", state=DISABLED)
        
    if E1Clicked == False:
        E1.configure(fg="black", bg="white", state=DISABLED)
    if E2Clicked == False:
        E2.configure(fg="black", bg="white", state=DISABLED)
    if E3Clicked == False:
        E3.configure(fg="black", bg="white", state=DISABLED)
    if E4Clicked == False:
        E4.configure(fg="black", bg="white", state=DISABLED)
    if E5Clicked == False:
        E5.configure(fg="black", bg="white", state=DISABLED)
    if E6Clicked == False:
        E6.configure(fg="black", bg="white", state=DISABLED)
    if E7Clicked == False:
        E7.configure(fg="black", bg="white", state=DISABLED)
    if E8Clicked == False:
        E8.configure(fg="black", bg="white", state=DISABLED)
    if E9Clicked == False:
        E9.configure(fg="black", bg="white", state=DISABLED)
        
    if F1Clicked == False:
        F1.configure(fg="black", bg="white", state=DISABLED)
    if F2Clicked == False:
        F2.configure(fg="black", bg="white", state=DISABLED)
    if F3Clicked == False:
        F3.configure(fg="black", bg="white", state=DISABLED)
    if F4Clicked == False:
        F4.configure(fg="black", bg="white", state=DISABLED)
    if F5Clicked == False:
        F5.configure(fg="black", bg="white", state=DISABLED)
    if F6Clicked == False:
        F6.configure(fg="black", bg="white", state=DISABLED)
    if F7Clicked == False:
        F7.configure(fg="black", bg="white", state=DISABLED)
    if F8Clicked == False:
        F8.configure(fg="black", bg="white", state=DISABLED)
    if F9Clicked == False:
        F9.configure(fg="black", bg="white", state=DISABLED)
        
    if G1Clicked == False:
        G1.configure(fg="black", bg="white", state=DISABLED)
    if G2Clicked == False:
        G2.configure(fg="black", bg="white", state=DISABLED)
    if G3Clicked == False:
        G3.configure(fg="black", bg="white", state=DISABLED)
    if G4Clicked == False:
        G4.configure(fg="black", bg="white", state=DISABLED)
    if G5Clicked == False:
        G5.configure(fg="black", bg="white", state=DISABLED)
    if G6Clicked == False:
        G6.configure(fg="black", bg="white", state=DISABLED)
    if G7Clicked == False:
        G7.configure(fg="black", bg="white", state=DISABLED)
    if G8Clicked == False:
        G8.configure(fg="black", bg="white", state=DISABLED)
    if G9Clicked == False:
        G9.configure(fg="black", bg="white", state=DISABLED)
    
    if H1Clicked == False:
        H1.configure(fg="black", bg="white", state=DISABLED)
    if H2Clicked == False:
        H2.configure(fg="black", bg="white", state=DISABLED)
    if H3Clicked == False:
        H3.configure(fg="black", bg="white", state=DISABLED)
    if H4Clicked == False:
        H4.configure(fg="black", bg="white", state=DISABLED)
    if H5Clicked == False:
        H5.configure(fg="black", bg="white", state=DISABLED)
    if H6Clicked == False:
        H6.configure(fg="black", bg="white", state=DISABLED)
    if H7Clicked == False:
        H7.configure(fg="black", bg="white", state=DISABLED)
    if H8Clicked == False:
        H8.configure(fg="black", bg="white", state=DISABLED)
    if H9Clicked == False:
        H9.configure(fg="black", bg="white", state=DISABLED)
        
    if I1Clicked == False:
        I1.configure(fg="black", bg="white", state=DISABLED)
    if I2Clicked == False:
        I2.configure(fg="black", bg="white", state=DISABLED)
    if I3Clicked == False:
        I3.configure(fg="black", bg="white", state=DISABLED)
    if I4Clicked == False:
        I4.configure(fg="black", bg="white", state=DISABLED)
    if I5Clicked == False:
        I5.configure(fg="black", bg="white", state=DISABLED)
    if I6Clicked == False:
        I6.configure(fg="black", bg="white", state=DISABLED)
    if I7Clicked == False:
        I7.configure(fg="black", bg="white", state=DISABLED)
    if I8Clicked == False:
        I8.configure(fg="black", bg="white", state=DISABLED)
    if I9Clicked == False:
        I9.configure(fg="black", bg="white", state=DISABLED)


def xAy1():
    global A1Clicked
    A1Clicked = not A1Clicked 
    
    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")

    A1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A1')")

    for row in cursor.execute("select * from board_details "): print(row)

    connection.commit()


    

def xAy2():
    global A2Clicked
    A2Clicked = not A2Clicked

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A2.configure(fg="black", bg="green", state=DISABLED)
    
    if p1shipcount >= 17:
       shiplimit()

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A2')")
    
    for row in cursor.execute("select * from board_details "): print(row)

    connection.commit()



def xAy3():
    global A3Clicked
    A3Clicked = not A3Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xAy4():
    global A4Clicked
    A4Clicked = not A4Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xAy5():
    global A5Clicked
    A5Clicked = not A5Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xAy6():
    global A6Clicked
    A6Clicked = not A6Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xAy7():
    global A7Clicked
    A7Clicked = not A7Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xAy8():
    global A8Clicked
    A8Clicked = not A8Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xAy9():
    global A9Clicked
    A9Clicked = not A9Clicked

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    A9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()


 
def xBy1():
    global B1Clicked
    B1Clicked = not B1Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xBy2():
    global B2Clicked
    B2Clicked = not B2Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xBy3():
    global B3Clicked
    B3Clicked = not B3Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xBy4():
    global B4Clicked
    B4Clicked = not B4Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xBy5():
    global B5Clicked
    B5Clicked = not B5Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B5.configure(fg="black", bg="green", state=DISABLED)
    
    if p1shipcount >= 17:
       shiplimit()

def xBy6():
    global B6Clicked
    B6Clicked = not B6Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B6.configure(fg="black", bg="green", state=DISABLED)
    
    if p1shipcount >= 17:
       shiplimit()

def xBy7():
    global B7Clicked
    B7Clicked = not B7Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B7.configure(fg="black", bg="green", state=DISABLED)
    
    if p1shipcount >= 17:
       shiplimit()

def xBy8():
    global B8Clicked
    B8Clicked = not B8Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B8.configure(fg="black", bg="green", state=DISABLED)
    
    if p1shipcount >= 17:
       shiplimit()

def xBy9():
    global B9Clicked
    B9Clicked = not B9Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    B9.configure(fg="black", bg="green", state=DISABLED)
    
    if p1shipcount >= 17:
       shiplimit()

 

    
def xCy1():
    global C1Clicked
    C1Clicked = not C1Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy2():
    global C2Clicked
    C2Clicked = not C2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy3():
    global C3Clicked
    C3Clicked = not C3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy4():
    global C4Clicked
    C4Clicked = not C4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy5():
    global C5Clicked
    C5Clicked = not C5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy6():
    global C6Clicked
    C6Clicked = not C6Clicked  
     
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy7():
    global C7Clicked
    C7Clicked = not C7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy8():
    global C8Clicked
    C8Clicked = not C8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xCy9():
    global C9Clicked
    C9Clicked = not C9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    C9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()



 
def xDy1():
    global D1Clicked
    D1Clicked = not D1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy2():
    global D2Clicked
    D2Clicked = not D2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy3():
    global D3Clicked
    D3Clicked = not D3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy4():
    global D4Clicked
    D4Clicked = not D4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy5():
    global D5Clicked
    D5Clicked = not D5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy6():
    global D6Clicked
    D6Clicked = not D6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy7():
    global D7Clicked
    D7Clicked = not D7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy8():
    global D8Clicked
    D8Clicked = not D8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xDy9():
    global D9Clicked
    D9Clicked = not D9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    D9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()



def xEy1():
    global E1Clicked
    E1Clicked = not E1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy2():
    global E2Clicked
    E2Clicked = not E2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy3():
    global E3Clicked
    E3Clicked = not E3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy4():
    global E4Clicked
    E4Clicked = not E4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy5():
    global E5Clicked
    E5Clicked = not E5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy6():
    global E6Clicked
    E6Clicked = not E6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy7():
    global E7Clicked
    E7Clicked = not E7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy8():
    global E8Clicked
    E8Clicked = not E8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xEy9():
    global E9Clicked
    E9Clicked = not E9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    E9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()




def xFy1():
    global F1Clicked
    F1Clicked = not F1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy2():
    global F2Clicked
    F2Clicked = not F2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy3():
    global F3Clicked
    F3Clicked = not F3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy4():
    global F4Clicked
    F4Clicked = not F4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy5():
    global F5Clicked
    F5Clicked = not F5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy6():
    global F6Clicked
    F6Clicked = not F6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy7():
    global F7Clicked
    F7Clicked = not F7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy8():
    global F8Clicked
    F8Clicked = not F8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xFy9():
    global F9Clicked
    F9Clicked = not F9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    F9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()




def xGy1():
    global G1Clicked
    G1Clicked = not G1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy2():
    global G2Clicked
    G2Clicked = not G2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy3():
    global G3Clicked
    G3Clicked = not G3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy4():
    global G4Clicked
    G4Clicked = not G4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy5():
    global G5Clicked
    G5Clicked = not G5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy6():
    global G6Clicked
    G6Clicked = not G6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy7():
    global G7Clicked
    G7Clicked = not G7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy8():
    global G8Clicked
    G8Clicked = not G8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xGy9():
    global G9Clicked
    G9Clicked = not G9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    G9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()




def xHy1():
    global H1Clicked
    H1Clicked = not H1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy2():
    global H2Clicked
    H2Clicked = not H2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy3():
    global H3Clicked
    H3Clicked = not H3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy4():
    global H4Clicked
    H4Clicked = not H4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy5():
    global H5Clicked
    H5Clicked = not H5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy6():
    global H6Clicked
    H6Clicked = not H6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy7():
    global H7Clicked
    H7Clicked = not H7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy8():
    global H8Clicked
    H8Clicked = not H8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xHy9():
    global H9Clicked
    H9Clicked = not H9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    H9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()




def xIy1():
    global I1Clicked
    I1Clicked = not I1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I1.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy2():
    global I2Clicked
    I2Clicked = not I2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I2.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy3():
    global I3Clicked
    I3Clicked = not I3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I3.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy4():
    global I4Clicked
    I4Clicked = not I4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I4.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy5():
    global I5Clicked
    I5Clicked = not I5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I5.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy6():
    global I6Clicked
    I6Clicked = not I6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I6.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy7():
    global I7Clicked
    I7Clicked = not I7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I7.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy8():
    global I8Clicked
    I8Clicked = not I8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I8.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()

def xIy9():
    global I9Clicked
    I9Clicked = not I9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1shipcount
    p1shipcount += 1  # Update value of global variable.
    countlabel.config(text= (p1shipcount, " ship grids chosen"))
    print(p1shipcount , " ship grids placed")


    I9.configure(fg="black", bg="green", state=DISABLED)

    if p1shipcount >= 17:
       shiplimit()



A1 = Button(board1, text="A1", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xAy1,)
A2 = Button(board1, text="A2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy2)
A3 = Button(board1, text="A3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy3)
A4 = Button(board1, text="A4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy4)
A5 = Button(board1, text="A5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy5)
A6 = Button(board1, text="A6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy6)
A7 = Button(board1, text="A7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy7)
A8 = Button(board1, text="A8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy8)
A9 = Button(board1, text="A9", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xAy9)


B1 = Button(board1, text="B1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy1)
B2 = Button(board1, text="B2", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy2)
B3 = Button(board1, text="B3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy3)
B4 = Button(board1, text="B4", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy4)
B5 = Button(board1, text="B5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy5)
B6 = Button(board1, text="B6", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy6)
B7 = Button(board1, text="B7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy7)
B8 = Button(board1, text="B8", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy8)
B9 = Button(board1, text="B9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy9)


C1 = Button(board1, text="C1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy1)
C2 = Button(board1, text="C2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy2)
C3 = Button(board1, text="C3", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xCy3)
C4 = Button(board1, text="C4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy4)
C5 = Button(board1, text="C5", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xCy5)
C6 = Button(board1, text="C6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy6)
C7 = Button(board1, text="C7", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xCy7)
C8 = Button(board1, text="C8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy8)
C9 = Button(board1, text="C9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy9)


D1 = Button(board1, text="D1", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xDy1)
D2 = Button(board1, text="D2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy2)
D3 = Button(board1, text="D3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy3)
D4 = Button(board1, text="D4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy4)
D5 = Button(board1, text="D5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy5)
D6 = Button(board1, text="D6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy6)
D7 = Button(board1, text="D7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy7)
D8 = Button(board1, text="D8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy8)
D9 = Button(board1, text="D9", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xDy9)


E1 = Button(board1, text="E1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy1)
E2 = Button(board1, text="E2", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy2)
E3 = Button(board1, text="E3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy3)
E4 = Button(board1, text="E4", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy4)
E5 = Button(board1, text="E5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy5)
E6 = Button(board1, text="E6", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy6)
E7 = Button(board1, text="E7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy7)
E8 = Button(board1, text="E8", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy8)
E9 = Button(board1, text="E9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy9)


F1 = Button(board1, text="F1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy1)
F2 = Button(board1, text="F2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy2)
F3 = Button(board1, text="F3", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xFy3)
F4 = Button(board1, text="F4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy4)
F5 = Button(board1, text="F5", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xFy5)
F6 = Button(board1, text="F6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy6)
F7 = Button(board1, text="F7", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xFy7)
F8 = Button(board1, text="F8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy8)
F9 = Button(board1, text="F9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy9)


G1 = Button(board1, text="G1", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xGy1)
G2 = Button(board1, text="G2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy2)
G3 = Button(board1, text="G3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy3)
G4 = Button(board1, text="G4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy4)
G5 = Button(board1, text="G5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy5)
G6 = Button(board1, text="G6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy6)
G7 = Button(board1, text="G7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy7)
G8 = Button(board1, text="G8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy8)
G9 = Button(board1, text="G9", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xGy9)


H1 = Button(board1, text="H1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy1)
H2 = Button(board1, text="H2", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy2)
H3 = Button(board1, text="H3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy3)
H4 = Button(board1, text="H4", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy4)
H5 = Button(board1, text="H5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy5)
H6 = Button(board1, text="H6", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy6)
H7 = Button(board1, text="H7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy7)
H8 = Button(board1, text="H8", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy8)
H9 = Button(board1, text="H9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy9)


I1 = Button(board1, text="I1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy1)
I2 = Button(board1, text="I2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy2)
I3 = Button(board1, text="I3", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xIy3)
I4 = Button(board1, text="I4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy4)
I5 = Button(board1, text="I5", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xIy5)
I6 = Button(board1, text="I6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy6)
I7 = Button(board1, text="I7", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xIy7)
I8 = Button(board1, text="I8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy8)
I9 = Button(board1, text="I9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy9)


A1.grid(row = 0, column = 0,)
A2.grid(row = 1, column = 0,)
A3.grid(row = 2, column = 0,)
A4.grid(row = 3, column = 0,)
A5.grid(row = 4, column = 0,)
A6.grid(row = 5, column = 0,)
A7.grid(row = 6, column = 0,)
A8.grid(row = 7, column = 0,)
A9.grid(row = 8, column = 0,)

B1.grid(row = 0, column = 1,)
B2.grid(row = 1, column = 1,)
B3.grid(row = 2, column = 1,)
B4.grid(row = 3, column = 1,)
B5.grid(row = 4, column = 1,)
B6.grid(row = 5, column = 1,)
B7.grid(row = 6, column = 1,)
B8.grid(row = 7, column = 1,)
B9.grid(row = 8, column = 1,)

C1.grid(row = 0, column = 2,)
C2.grid(row = 1, column = 2,)
C3.grid(row = 2, column = 2,)
C4.grid(row = 3, column = 2,)
C5.grid(row = 4, column = 2,)
C6.grid(row = 5, column = 2,)
C7.grid(row = 6, column = 2,)
C8.grid(row = 7, column = 2,)
C9.grid(row = 8, column = 2,)

D1.grid(row = 0, column = 3,)
D2.grid(row = 1, column = 3,)
D3.grid(row = 2, column = 3,)
D4.grid(row = 3, column = 3,)
D5.grid(row = 4, column = 3,)
D6.grid(row = 5, column = 3,)
D7.grid(row = 6, column = 3,)
D8.grid(row = 7, column = 3,)
D9.grid(row = 8, column = 3,)

E1.grid(row = 0, column = 4,)
E2.grid(row = 1, column = 4,)
E3.grid(row = 2, column = 4,)
E4.grid(row = 3, column = 4,)
E5.grid(row = 4, column = 4,)
E6.grid(row = 5, column = 4,)
E7.grid(row = 6, column = 4,)
E8.grid(row = 7, column = 4,)
E9.grid(row = 8, column = 4,)

F1.grid(row = 0, column = 5,)
F2.grid(row = 1, column = 5,)
F3.grid(row = 2, column = 5,)
F4.grid(row = 3, column = 5,)
F5.grid(row = 4, column = 5,)
F6.grid(row = 5, column = 5,)
F7.grid(row = 6, column = 5,)
F8.grid(row = 7, column = 5,)
F9.grid(row = 8, column = 5,)

G1.grid(row = 0, column = 6,)
G2.grid(row = 1, column = 6,)
G3.grid(row = 2, column = 6,)
G4.grid(row = 3, column = 6,)
G5.grid(row = 4, column = 6,)
G6.grid(row = 5, column = 6,)
G7.grid(row = 6, column = 6,)
G8.grid(row = 7, column = 6,)
G9.grid(row = 8, column = 6,)

H1.grid(row = 0, column = 7,)
H2.grid(row = 1, column = 7,)
H3.grid(row = 2, column = 7,)
H4.grid(row = 3, column = 7,)
H5.grid(row = 4, column = 7,)
H6.grid(row = 5, column = 7,)
H7.grid(row = 6, column = 7,)
H8.grid(row = 7, column = 7,)
H9.grid(row = 8, column = 7,)

I1.grid(row = 0, column = 8,)
I2.grid(row = 1, column = 8,)
I3.grid(row = 2, column = 8,)
I4.grid(row = 3, column = 8,)
I5.grid(row = 4, column = 8,)
I6.grid(row = 5, column = 8,)
I7.grid(row = 6, column = 8,)
I8.grid(row = 7, column = 8,)
I9.grid(row = 8, column = 8,)




root.mainloop()