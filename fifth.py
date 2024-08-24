from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlite3
from tkinter import messagebox 


root = Tk()
root.title("PLAYER 1 GUESS PLAYER 2 SHIP PLACEMENTS")

root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.geometry("900x600")
root.configure(background="light green")


connection = sqlite3.connect("battleships.db")
cursor =connection.cursor()


cursor.execute("create table if not exists board_details(player1_ships text, player2_ships text, player1_guess text, player2_guess text)")

#board_list = {"A1 bool, A2 bool, A3 bool, A4 bool, A5 bool, A6 bool, A7 bool, A8 bool, A9 bool, B1 bool, B2 bool, B3 bool, B4 bool, B5 bool, B6 bool, B7 bool, B8 bool, B9 bool, C1 bool, C2 bool, C3 bool, C4 bool, C5 bool, C6 bool, C7 bool, C8 bool, C9 bool"}
#cursor.execute("create table if not exists p1_reveals('{}')".format(board_list))
#cursor.execute("create table if not exists p2_reveals(A1 bool, A2 bool, A3 bool, A4 bool, A5 bool, A6 bool, A7 bool, A8 bool, A9 bool, B1 bool, B2 bool, B3 bool, B4 bool, B5 bool, B6 bool, B7 bool, B8 bool, B9 bool, C1 bool, C2 bool, C3 bool, C4 bool, C5 bool, C6 bool, C7 bool, C8 bool, C9 bool, D1 bool, D2 bool, D3 bool, D4 bool, D5 bool, D6 bool, D7 bool, D8 bool, D9 bool, E1 bool, E2 bool, E3 bool, E4 bool, E5 bool, E6 bool, E7 bool, E8 bool, E9 bool, F1 bool, F2 bool, F3 bool, F4 bool, F5 bool, F6 bool, F7 bool, F8 bool, F9 bool, G1 bool, G2 bool, G3 bool, G4 bool, G5 bool, G6 bool, G7 bool, G8 bool, G9 bool, H1 bool, H2 bool, H3 bool, H4 bool, H5 bool, H6 bool, H7 bool, H8 bool, H9 bool, I1 bool, I2 bool, I3 bool, I4 bool, I5 bool, I6 bool, I7 bool, I8 bool, I9 bool)")

cursor.execute("""
    create table if not exists 
        p1_reveals(
            A1 bool, 
            A2 bool, 
            A3 bool, 
            A4 bool, 
            A5 bool, 
            A6 bool, 
            A7 bool, 
            A8 bool, 
            A9 bool, 
            B1 bool, 
            B2 bool, 
            B3 bool, 
            B4 bool, 
            B5 bool, 
            B6 bool, 
            B7 bool, 
            B8 bool, 
            B9 bool, 
            C1 bool, 
            C2 bool, 
            C3 bool, 
            C4 bool, 
            C5 bool, 
            C6 bool, 
            C7 bool, 
            C8 bool, 
            C9 bool, 
            D1 bool, 
            D2 bool, 
            D3 bool, 
            D4 bool, 
            D5 bool, 
            D6 bool, 
            D7 bool, 
            D8 bool, 
            D9 bool, 
            E1 bool, 
            E2 bool, 
            E3 bool, 
            E4 bool, 
            E5 bool, 
            E6 bool, 
            E7 bool, 
            E8 bool, 
            E9 bool, 
            F1 bool, 
            F2 bool, 
            F3 bool, 
            F4 bool, 
            F5 bool, 
            F6 bool, 
            F7 bool, 
            F8 bool, 
            F9 bool, 
            G1 bool, 
            G2 bool, 
            G3 bool, 
            G4 bool, 
            G5 bool, 
            G6 bool, 
            G7 bool, 
            G8 bool, 
            G9 bool, 
            H1 bool, 
            H2 bool, 
            H3 bool, 
            H4 bool, 
            H5 bool, 
            H6 bool, 
            H7 bool, 
            H8 bool, 
            H9 bool, 
            I1 bool, 
            I2 bool, 
            I3 bool, 
            I4 bool, 
            I5 bool, 
            I6 bool, 
            I7 bool, 
            I8 bool, 
            I9 bool
                )""")
connection.commit()


board3 = Frame(root, background="light green")
board3.place(relx=0.5, rely=0.5, anchor= CENTER,)


def gamequit():
    cursor.execute("DROP TABLE board_details")
    cursor.execute("DROP TABLE p1_reveals")
    cursor.execute("DROP TABLE p2_reveals")
    messagebox.showinfo("BATTLESHIPS", "killing game")
    root.quit()

button_exit = Button(board3, text="Exit Program", bg="yellow", activebackground="red", activeforeground="white", command = gamequit )
button_exit.grid(row=9, column=9)


def p1guessing():
    if p1guesscount < 1:
        messagebox.showinfo("!!!PLAYER 1!!!","GUESS 1 SHIP FROM PLAYER 2 BEFORE CONFIRMATION")

    else:
        guesscheck()
        cursor.execute("UPDATE board_details SET player1_guess = NULL")
        cursor.execute("DELETE FROM board_details WHERE player1_ships IS NULL AND player2_ships IS NULL AND player1_guess IS NULL")
        connection.commit()        
        messagebox.showinfo("PLAYER 1 GUESSED A SHIP POSITION", "NOW PLAYER 2 GETS TO GUESS ONE OF YOUR SHIP LOCATIONS")
        root.destroy()
        subprocess.run(["python", ("sixth.py")])


def p1resetguess(): 
    cursor.execute("UPDATE board_details SET player1_guess = NULL")
    cursor.execute("DELETE FROM board_details WHERE player1_ships IS NULL AND player2_ships IS NULL AND player1_guess IS NULL")
    connection.commit()
    messagebox.showinfo("PLAYER 1 BOARD", "PLAYER 2 SHIP GUESS RESET")
    root.destroy()
    subprocess.run(["python", ("fifth.py")])


p1_con_place = Button(root, text="CONFIRM GUESS", padx = 10, pady = 5, fg="orange", bg="black", activebackground="orange", activeforeground="black", command = p1guessing)
p1_con_place.grid()

p1_res_place = Button(root, text="reset guess", padx = 10, pady = 5, fg="orange", bg="black", activebackground="orange", activeforeground="black",command = p1resetguess)
p1_res_place.grid()


def p1winning():
    messagebox.showinfo("PLAYER 1 WINS", "player 1 hit all of player 2's ships")
    gamequit()

#Define global guess count.
p1guesscount = 0
p1wincon = 0

playerlabel = Label(text="PLAYER 1:", bg="light green")
playerlabel.grid(row=7, column=0)

#count display
countlabel = Button(root, text = "guess an enemy ship location", bg="light green", activebackground="light yellow")
countlabel.grid(row = 9, column = 0, columnspan = 2,)

limitlabel = Label(text="(you only get one guess)", bg="light green")
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


def guesslimit():
    
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
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A1')")

    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grid guessed"))
    print(p1guesscount , " ship grid guessed")

    A1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()
    

def xAy2():
    global A2Clicked
    A2Clicked = not A2Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A2.configure(fg="black", bg="green", state=DISABLED)
    
    if p1guesscount >= 1:
       guesslimit()

def xAy3():
    global A3Clicked
    A3Clicked = not A3Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xAy4():
    global A4Clicked
    A4Clicked = not A4Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xAy5():
    global A5Clicked
    A5Clicked = not A5Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xAy6():
    global A6Clicked
    A6Clicked = not A6Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xAy7():
    global A7Clicked
    A7Clicked = not A7Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xAy8():
    global A8Clicked
    A8Clicked = not A8Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xAy9():
    global A9Clicked
    A9Clicked = not A9Clicked

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    A9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()


 
def xBy1():
    global B1Clicked
    B1Clicked = not B1Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xBy2():
    global B2Clicked
    B2Clicked = not B2Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xBy3():
    global B3Clicked
    B3Clicked = not B3Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xBy4():
    global B4Clicked
    B4Clicked = not B4Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xBy5():
    global B5Clicked
    B5Clicked = not B5Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B5.configure(fg="black", bg="green", state=DISABLED)
    
    if p1guesscount >= 1:
       guesslimit()

def xBy6():
    global B6Clicked
    B6Clicked = not B6Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B6.configure(fg="black", bg="green", state=DISABLED)
    
    if p1guesscount >= 1:
       guesslimit()

def xBy7():
    global B7Clicked
    B7Clicked = not B7Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B7.configure(fg="black", bg="green", state=DISABLED)
    
    if p1guesscount >= 1:
       guesslimit()

def xBy8():
    global B8Clicked
    B8Clicked = not B8Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B8.configure(fg="black", bg="green", state=DISABLED)
    
    if p1guesscount >= 1:
       guesslimit()

def xBy9():
    global B9Clicked
    B9Clicked = not B9Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    B9.configure(fg="black", bg="green", state=DISABLED)
    
    if p1guesscount >= 1:
       guesslimit()

 

    
def xCy1():
    global C1Clicked
    C1Clicked = not C1Clicked 
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy2():
    global C2Clicked
    C2Clicked = not C2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy3():
    global C3Clicked
    C3Clicked = not C3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy4():
    global C4Clicked
    C4Clicked = not C4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy5():
    global C5Clicked
    C5Clicked = not C5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy6():
    global C6Clicked
    C6Clicked = not C6Clicked  
     
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy7():
    global C7Clicked
    C7Clicked = not C7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy8():
    global C8Clicked
    C8Clicked = not C8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xCy9():
    global C9Clicked
    C9Clicked = not C9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    C9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()



 
def xDy1():
    global D1Clicked
    D1Clicked = not D1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy2():
    global D2Clicked
    D2Clicked = not D2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy3():
    global D3Clicked
    D3Clicked = not D3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy4():
    global D4Clicked
    D4Clicked = not D4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy5():
    global D5Clicked
    D5Clicked = not D5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy6():
    global D6Clicked
    D6Clicked = not D6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy7():
    global D7Clicked
    D7Clicked = not D7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy8():
    global D8Clicked
    D8Clicked = not D8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xDy9():
    global D9Clicked
    D9Clicked = not D9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    D9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()



def xEy1():
    global E1Clicked
    E1Clicked = not E1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy2():
    global E2Clicked
    E2Clicked = not E2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy3():
    global E3Clicked
    E3Clicked = not E3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy4():
    global E4Clicked
    E4Clicked = not E4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy5():
    global E5Clicked
    E5Clicked = not E5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy6():
    global E6Clicked
    E6Clicked = not E6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy7():
    global E7Clicked
    E7Clicked = not E7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy8():
    global E8Clicked
    E8Clicked = not E8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xEy9():
    global E9Clicked
    E9Clicked = not E9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    E9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()




def xFy1():
    global F1Clicked
    F1Clicked = not F1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy2():
    global F2Clicked
    F2Clicked = not F2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy3():
    global F3Clicked
    F3Clicked = not F3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy4():
    global F4Clicked
    F4Clicked = not F4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy5():
    global F5Clicked
    F5Clicked = not F5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy6():
    global F6Clicked
    F6Clicked = not F6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy7():
    global F7Clicked
    F7Clicked = not F7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy8():
    global F8Clicked
    F8Clicked = not F8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xFy9():
    global F9Clicked
    F9Clicked = not F9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    F9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()




def xGy1():
    global G1Clicked
    G1Clicked = not G1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy2():
    global G2Clicked
    G2Clicked = not G2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy3():
    global G3Clicked
    G3Clicked = not G3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy4():
    global G4Clicked
    G4Clicked = not G4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy5():
    global G5Clicked
    G5Clicked = not G5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy6():
    global G6Clicked
    G6Clicked = not G6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy7():
    global G7Clicked
    G7Clicked = not G7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy8():
    global G8Clicked
    G8Clicked = not G8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xGy9():
    global G9Clicked
    G9Clicked = not G9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    G9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()




def xHy1():
    global H1Clicked
    H1Clicked = not H1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy2():
    global H2Clicked
    H2Clicked = not H2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy3():
    global H3Clicked
    H3Clicked = not H3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy4():
    global H4Clicked
    H4Clicked = not H4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy5():
    global H5Clicked
    H5Clicked = not H5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy6():
    global H6Clicked
    H6Clicked = not H6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy7():
    global H7Clicked
    H7Clicked = not H7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy8():
    global H8Clicked
    H8Clicked = not H8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xHy9():
    global H9Clicked
    H9Clicked = not H9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    H9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()




def xIy1():
    global I1Clicked
    I1Clicked = not I1Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I1.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy2():
    global I2Clicked
    I2Clicked = not I2Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I2.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy3():
    global I3Clicked
    I3Clicked = not I3Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I3.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy4():
    global I4Clicked
    I4Clicked = not I4Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I4.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy5():
    global I5Clicked
    I5Clicked = not I5Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I5.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy6():
    global I6Clicked
    I6Clicked = not I6Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I6.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy7():
    global I7Clicked
    I7Clicked = not I7Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I7.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy8():
    global I8Clicked
    I8Clicked = not I8Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I8.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()

def xIy9():
    global I9Clicked
    I9Clicked = not I9Clicked  
    
    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global p1guesscount
    p1guesscount += 1  # Update value of global variable.
    countlabel.config(text= (p1guesscount, " ship grids chosen"))
    print(p1guesscount , " ship grids placed")


    I9.configure(fg="black", bg="green", state=DISABLED)

    if p1guesscount >= 1:
       guesslimit()



A1 = Button(board3, text="A1", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xAy1,)
A2 = Button(board3, text="A2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy2)
A3 = Button(board3, text="A3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy3)
A4 = Button(board3, text="A4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy4)
A5 = Button(board3, text="A5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy5)
A6 = Button(board3, text="A6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy6)
A7 = Button(board3, text="A7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy7)
A8 = Button(board3, text="A8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xAy8)
A9 = Button(board3, text="A9", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xAy9)


B1 = Button(board3, text="B1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy1)
B2 = Button(board3, text="B2", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy2)
B3 = Button(board3, text="B3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy3)
B4 = Button(board3, text="B4", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy4)
B5 = Button(board3, text="B5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy5)
B6 = Button(board3, text="B6", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy6)
B7 = Button(board3, text="B7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy7)
B8 = Button(board3, text="B8", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xBy8)
B9 = Button(board3, text="B9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xBy9)


C1 = Button(board3, text="C1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy1)
C2 = Button(board3, text="C2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy2)
C3 = Button(board3, text="C3", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xCy3)
C4 = Button(board3, text="C4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy4)
C5 = Button(board3, text="C5", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xCy5)
C6 = Button(board3, text="C6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy6)
C7 = Button(board3, text="C7", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xCy7)
C8 = Button(board3, text="C8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy8)
C9 = Button(board3, text="C9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xCy9)


D1 = Button(board3, text="D1", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xDy1)
D2 = Button(board3, text="D2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy2)
D3 = Button(board3, text="D3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy3)
D4 = Button(board3, text="D4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy4)
D5 = Button(board3, text="D5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy5)
D6 = Button(board3, text="D6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy6)
D7 = Button(board3, text="D7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy7)
D8 = Button(board3, text="D8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xDy8)
D9 = Button(board3, text="D9", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xDy9)


E1 = Button(board3, text="E1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy1)
E2 = Button(board3, text="E2", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy2)
E3 = Button(board3, text="E3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy3)
E4 = Button(board3, text="E4", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy4)
E5 = Button(board3, text="E5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy5)
E6 = Button(board3, text="E6", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy6)
E7 = Button(board3, text="E7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy7)
E8 = Button(board3, text="E8", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xEy8)
E9 = Button(board3, text="E9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xEy9)


F1 = Button(board3, text="F1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy1)
F2 = Button(board3, text="F2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy2)
F3 = Button(board3, text="F3", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xFy3)
F4 = Button(board3, text="F4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy4)
F5 = Button(board3, text="F5", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xFy5)
F6 = Button(board3, text="F6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy6)
F7 = Button(board3, text="F7", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xFy7)
F8 = Button(board3, text="F8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy8)
F9 = Button(board3, text="F9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xFy9)


G1 = Button(board3, text="G1", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xGy1)
G2 = Button(board3, text="G2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy2)
G3 = Button(board3, text="G3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy3)
G4 = Button(board3, text="G4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy4)
G5 = Button(board3, text="G5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy5)
G6 = Button(board3, text="G6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy6)
G7 = Button(board3, text="G7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy7)
G8 = Button(board3, text="G8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xGy8)
G9 = Button(board3, text="G9", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xGy9)


H1 = Button(board3, text="H1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy1)
H2 = Button(board3, text="H2", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy2)
H3 = Button(board3, text="H3", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy3)
H4 = Button(board3, text="H4", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy4)
H5 = Button(board3, text="H5", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy5)
H6 = Button(board3, text="H6", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy6)
H7 = Button(board3, text="H7", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy7)
H8 = Button(board3, text="H8", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xHy8)
H9 = Button(board3, text="H9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xHy9)


I1 = Button(board3, text="I1", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy1)
I2 = Button(board3, text="I2", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy2)
I3 = Button(board3, text="I3", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xIy3)
I4 = Button(board3, text="I4", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy4)
I5 = Button(board3, text="I5", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xIy5)
I6 = Button(board3, text="I6", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy6)
I7 = Button(board3, text="I7", padx = 15, pady = 15, fg="white", bg="blue", activebackground="hot pink", command = xIy7)
I8 = Button(board3, text="I8", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy8)
I9 = Button(board3, text="I9", padx = 15, pady = 15, fg="black", bg="light blue", activebackground="hot pink", command = xIy9)


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



def ship_history():
    global p1wincon
    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A1')"):
                if row == (0,):
                    print("A1 - miss")
                    A1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A1 - hit")
                    A1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A2')"):
                if row == (0,):
                    print("A2 - miss")
                    A2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A2 - hit")
                    A2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A3')"):
                if row == (0,):
                    print("A3 - miss")
                    A3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A3 - hit")
                    A3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A4')"):
                if row == (0,):
                    print("A4 - miss")
                    A4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A4 - hit")
                    A4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A5')"):
                if row == (0,):
                    print("A5 - miss")
                    A5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A5 - hit")
                    A5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A6')"):
                if row == (0,):
                    print("A6 - miss")
                    A6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A6 - hit")
                    A6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A7')"):
                if row == (0,):
                    print("A7 - miss")
                    A7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A7 - hit")
                    A7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A8')"):
                if row == (0,):
                    print("A8 - miss")
                    A8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A8 - hit")
                    A8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A9')"):
                if row == (0,):
                    print("A9 - miss")
                    A9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A9 - hit")
                    A9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B1')"):
                if row == (0,):
                    print("B1 - miss")
                    B1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B1 - hit")
                    B1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B2')"):
                if row == (0,):
                    print("B2 - miss")
                    B2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B2 - hit")
                    B2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B3')"):
                if row == (0,):
                    print("B3 - miss")
                    B3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B3 - hit")
                    B3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B4')"):
                if row == (0,):
                    print("B4 - miss")
                    B4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B4 - hit")
                    B4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B5')"):
                if row == (0,):
                    print("B5 - miss")
                    B5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B5 - hit")
                    B5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B6')"):
                if row == (0,):
                    print("B6 - miss")
                    B6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B6 - hit")
                    B6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B7')"):
                if row == (0,):
                    print("B7 - miss")
                    B7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B7 - hit")
                    B7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B8')"):
                if row == (0,):
                    print("B8 - miss")
                    B8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B8 - hit")
                    B8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B9')"):
                if row == (0,):
                    print("B9 - miss")
                    B9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B9 - hit")
                    B9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C1')"):
                if row == (0,):
                    print("C1 - miss")
                    C1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C1 - hit")
                    C1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C2')"):
                if row == (0,):
                    print("C2 - miss")
                    C2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C2 - hit")
                    C2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C3')"):
                if row == (0,):
                    print("C3 - miss")
                    C3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C3 - hit")
                    C3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C4')"):
                if row == (0,):
                    print("C4 - miss")
                    C4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C4 - hit")
                    C4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C5')"):
                if row == (0,):
                    print("C5 - miss")
                    C5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C5 - hit")
                    C5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C6')"):
                if row == (0,):
                    print("C6 - miss")
                    C6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C6 - hit")
                    C6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C7')"):
                if row == (0,):
                    print("C7 - miss")
                    C7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C7 - hit")
                    C7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C8')"):
                if row == (0,):
                    print("C8 - miss")
                    C8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C8 - hit")
                    C8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C9')"):
                if row == (0,):
                    print("C9 - miss")
                    C9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C9 - hit")
                    C9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D1')"):
                if row == (0,):
                    print("D1 - miss")
                    D1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D1 - hit")
                    D1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D2')"):
                if row == (0,):
                    print("D2 - miss")
                    D2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D2 - hit")
                    D2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D3')"):
                if row == (0,):
                    print("D3 - miss")
                    D3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D3 - hit")
                    D3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D4')"):
                if row == (0,):
                    print("D4 - miss")
                    D4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D4 - hit")
                    D4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D5')"):
                if row == (0,):
                    print("D5 - miss")
                    D5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D5 - hit")
                    D5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D6')"):
                if row == (0,):
                    print("D6 - miss")
                    D6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D6 - hit")
                    D6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D7')"):
                if row == (0,):
                    print("D7 - miss")
                    D7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D7 - hit")
                    D7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D8')"):
                if row == (0,):
                    print("D8 - miss")
                    D8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D8 - hit")
                    D8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D9')"):
                if row == (0,):
                    print("D9 - miss")
                    D9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D9 - hit")
                    D9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E1')"):
                if row == (0,):
                    print("E1 - miss")
                    E1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E1 - hit")
                    E1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E2')"):
                if row == (0,):
                    print("E2 - miss")
                    E2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E2 - hit")
                    E2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E3')"):
                if row == (0,):
                    print("E3 - miss")
                    E3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E3 - hit")
                    E3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E4')"):
                if row == (0,):
                    print("E4 - miss")
                    E4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E4 - hit")
                    E4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E5')"):
                if row == (0,):
                    print("E5 - miss")
                    E5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E5 - hit")
                    E5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E6')"):
                if row == (0,):
                    print("E6 - miss")
                    E6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E6 - hit")
                    E6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E7')"):
                if row == (0,):
                    print("E7 - miss")
                    E7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E7 - hit")
                    E7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E8')"):
                if row == (0,):
                    print("E8 - miss")
                    E8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E8 - hit")
                    E8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E9')"):
                if row == (0,):
                    print("E9 - miss")
                    E9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E9 - hit")
                    E9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F1')"):
                if row == (0,):
                    print("F1 - miss")
                    F1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F1 - hit")
                    F1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F2')"):
                if row == (0,):
                    print("F2 - miss")
                    F2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F2 - hit")
                    F2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F3')"):
                if row == (0,):
                    print("F3 - miss")
                    F3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F3 - hit")
                    F3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F4')"):
                if row == (0,):
                    print("F4 - miss")
                    F4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F4 - hit")
                    F4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F5')"):
                if row == (0,):
                    print("F5 - miss")
                    F5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F5 - hit")
                    F5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F6')"):
                if row == (0,):
                    print("F6 - miss")
                    F6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F6 - hit")
                    F6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F7')"):
                if row == (0,):
                    print("F7 - miss")
                    F7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F7 - hit")
                    F7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F8')"):
                if row == (0,):
                    print("F8 - miss")
                    F8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F8 - hit")
                    F8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F9')"):
                if row == (0,):
                    print("F9 - miss")
                    F9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F9 - hit")
                    F9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G1')"):
                if row == (0,):
                    print("G1 - miss")
                    G1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G1 - hit")
                    G1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G2')"):
                if row == (0,):
                    print("G2 - miss")
                    G2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G2 - hit")
                    G2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G3')"):
                if row == (0,):
                    print("G3 - miss")
                    G3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G3 - hit")
                    G3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G4')"):
                if row == (0,):
                    print("G4 - miss")
                    G4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G4 - hit")
                    G4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G5')"):
                if row == (0,):
                    print("G5 - miss")
                    G5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G5 - hit")
                    G5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G6')"):
                if row == (0,):
                    print("G6 - miss")
                    G6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G6 - hit")
                    G6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G7')"):
                if row == (0,):
                    print("G7 - miss")
                    G7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G7 - hit")
                    G7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G8')"):
                if row == (0,):
                    print("G8 - miss")
                    G8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G8 - hit")
                    G8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G9')"):
                if row == (0,):
                    print("G9 - miss")
                    G9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G9 - hit")
                    G9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H1')"):
                if row == (0,):
                    print("H1 - miss")
                    H1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H1 - hit")
                    H1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H2')"):
                if row == (0,):
                    print("H2 - miss")
                    H2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H2 - hit")
                    H2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H3')"):
                if row == (0,):
                    print("H3 - miss")
                    H3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H3 - hit")
                    H3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H4')"):
                if row == (0,):
                    print("H4 - miss")
                    H4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H4 - hit")
                    H4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H5')"):
                if row == (0,):
                    print("H5 - miss")
                    H5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H5 - hit")
                    H5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H6')"):
                if row == (0,):
                    print("H6 - miss")
                    H6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H6 - hit")
                    H6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H7')"):
                if row == (0,):
                    print("H7 - miss")
                    H7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H7 - hit")
                    H7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H8')"):
                if row == (0,):
                    print("H8 - miss")
                    H8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H8 - hit")
                    H8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H9')"):
                if row == (0,):
                    print("H9 - miss")
                    H9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H9 - hit")
                    H9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I1 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I1')"):
                if row == (0,):
                    print("I1 - miss")
                    I1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I1 - hit")
                    I1.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I2 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I2')"):
                if row == (0,):
                    print("I2 - miss")
                    I2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I2 - hit")
                    I2.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I3 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I3')"):
                if row == (0,):
                    print("I3 - miss")
                    I3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I3 - hit")
                    I3.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I4 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I4')"):
                if row == (0,):
                    print("I4 - miss")
                    I4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I4 - hit")
                    I4.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I5 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I5')"):
                if row == (0,):
                    print("I5 - miss")
                    I5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I5 - hit")
                    I5.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I6 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I6')"):
                if row == (0,):
                    print("I6 - miss")
                    I6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I6 - hit")
                    I6.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I7 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I7')"):
                if row == (0,):
                    print("I7 - miss")
                    I7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I7 - hit")
                    I7.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I8 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I8')"):
                if row == (0,):
                    print("I8 - miss")
                    I8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I8 - hit")
                    I8.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I9 = '1')"):
        if row == (1,):
            for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I9')"):
                if row == (0,):
                    print("I9 - miss")
                    I9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I9 - hit")
                    I9.configure(fg="black", bg="red", state=DISABLED)
                    
                    p1wincon += 1  # Update value of global variable.
                    print(p1wincon , "/17 player 2 ship grids found")
                    if p1wincon >= 17:
                        p1winning()


    connection.commit()


ship_history()




#cursor.execute("create table if not exists p1_reveals(A1 bool, A2 bool, A3 bool, A4 bool, A5 bool, A6 bool, A7 bool, A8 bool, A9 bool)")




# cursor.execute("SELECT * FROM board_details WHERE player1_ships = '{}' and player2_guess = '{}'".format(A1Clicked))

# for row in cursor.execute("select * from board_details "): print(row)

# connection.commit()

def guesscheck():
    if A1Clicked == True:     
        #cursor.execute("SELECT EXISTS(SELECT * FROM board_details WHERE player1_ships = 'A1' and player2_guess = 'A1')")
        
# for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player1_ships = 'A1' and player2_guess = 'A1')"):
# if row == (0,):
#     print("miss")
# if row == (1,):
#     print("hit")

        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A1')"):
            if row == (0,):
                print("A1 - miss")
                A1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A1 - hit")
                A1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A1) VALUES(1)")
        connection.commit()
        
        #cursor.execute("SELECT IF(EXISTS(SELECT * FROM board_details WHERE player1_ships = 'A1' and player2_guess = 'A1')) AS 'result' FROM board_details;")

        # if cursor.execute("SELECT * FROM board_details WHERE player1_ships = 'A1' and player2_guess = 'A1'"):
        #     A1.configure(fg="black", bg="red", state=DISABLED)
        #     print("A1 - HIT") 
        # elif cursor.execute("SELECT * FROM board_details WHERE player1_ships = 'A1' and player2_guess = 'A1'") :
        #     A1.configure(fg="black", bg="blue", state=DISABLED)
        #     print("A1 - miss")

    if A2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A2')"):
            if row == (0,):
                print("A2 - miss")
                A2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A2 - hit")
                A2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A2) VALUES(1)")
        connection.commit()

    if A3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A3')"):
            if row == (0,):
                print("A3 - miss")
                A3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A3 - hit")
                A3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A3) VALUES(1)")
        connection.commit()

    if A4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A4')"):
            if row == (0,):
                print("A4 - miss")
                A4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A4 - hit")
                A4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A4) VALUES(1)")
        connection.commit()

    if A5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A5')"):
            if row == (0,):
                print("A5 - miss")
                A5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A5 - hit")
                A5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A5) VALUES(1)")
        connection.commit()

    if A6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A6')"):
            if row == (0,):
                print("A6 - miss")
                A6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A6 - hit")
                A6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A6) VALUES(1)")
        connection.commit()

    if A7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A7')"):
            if row == (0,):
                print("A7 - miss")
                A7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A7 - hit")
                A7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A7) VALUES(1)")
        connection.commit()

    if A8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A8')"):
            if row == (0,):
                print("A8 - miss")
                A8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A8 - hit")
                A8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A8) VALUES(1)")
        connection.commit()

    if A9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'A9')"):
            if row == (0,):
                print("A9 - miss")
                A9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A9 - hit")
                A9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(A9) VALUES(1)")
        connection.commit()
    
    
    if B1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B1')"):
            if row == (0,):
                print("B1 - miss")
                B1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B1 - hit")
                B1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B1) VALUES(1)")
        connection.commit()

    if B2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B2')"):
            if row == (0,):
                print("B2 - miss")
                B2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B2 - hit")
                B2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B2) VALUES(1)")
        connection.commit()

    if B3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B3')"):
            if row == (0,):
                print("B3 - miss")
                B3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B3 - hit")
                B3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B3) VALUES(1)")
        connection.commit()

    if B4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B4')"):
            if row == (0,):
                print("B4 - miss")
                B4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B4 - hit")
                B4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B4) VALUES(1)")
        connection.commit()

    if B5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B5')"):
            if row == (0,):
                print("B5 - miss")
                B5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B5 - hit")
                B5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B5) VALUES(1)")
        connection.commit()

    if B6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B6')"):
            if row == (0,):
                print("B6 - miss")
                B6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B6 - hit")
                B6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B6) VALUES(1)")
        connection.commit()

    if B7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B7')"):
            if row == (0,):
                print("B7 - miss")
                B7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B7 - hit")
                B7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B7) VALUES(1)")
        connection.commit()

    if B8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B8')"):
            if row == (0,):
                print("B8 - miss")
                B8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B8 - hit")
                B8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B8) VALUES(1)")
        connection.commit()

    if B9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'B9')"):
            if row == (0,):
                print("B9 - miss")
                B9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B9 - hit")
                B9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(B9) VALUES(1)")
        connection.commit()


    if C1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C1')"):
            if row == (0,):
                print("C1 - miss")
                C1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C1 - hit")
                C1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C1) VALUES(1)")
        connection.commit()

    if C2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C2')"):
            if row == (0,):
                print("C2 - miss")
                C2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C2 - hit")
                C2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C2) VALUES(1)")
        connection.commit()

    if C3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C3')"):
            if row == (0,):
                print("C3 - miss")
                C3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C3 - hit")
                C3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C3) VALUES(1)")
        connection.commit()

    if C4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C4')"):
            if row == (0,):
                print("C4 - miss")
                C4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C4 - hit")
                C4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C4) VALUES(1)")
        connection.commit()

    if C5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C5')"):
            if row == (0,):
                print("C5 - miss")
                C5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C5 - hit")
                C5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C5) VALUES(1)")
        connection.commit()

    if C6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C6')"):
            if row == (0,):
                print("C6 - miss")
                C6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C6 - hit")
                C6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C6) VALUES(1)")
        connection.commit()

    if C7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C7')"):
            if row == (0,):
                print("C7 - miss")
                C7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C7 - hit")
                C7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C7) VALUES(1)")
        connection.commit()

    if C8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C8')"):
            if row == (0,):
                print("C8 - miss")
                C8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C8 - hit")
                C8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C8) VALUES(1)")
        connection.commit()

    if C9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'C9')"):
            if row == (0,):
                print("C9 - miss")
                C9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C9 - hit")
                C9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(C9) VALUES(1)")
        connection.commit()

        
    if D1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D1')"):
            if row == (0,):
                print("D1 - miss")
                D1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D1 - hit")
                D1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D1) VALUES(1)")
        connection.commit()

    if D2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D2')"):
            if row == (0,):
                print("D2 - miss")
                D2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D2 - hit")
                D2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D2) VALUES(1)")
        connection.commit()

    if D3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D3')"):
            if row == (0,):
                print("D3 - miss")
                D3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D3 - hit")
                D3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D3) VALUES(1)")
        connection.commit()

    if D4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D4')"):
            if row == (0,):
                print("D4 - miss")
                D4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D4 - hit")
                D4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D4) VALUES(1)")
        connection.commit()

    if D5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D5')"):
            if row == (0,):
                print("D5 - miss")
                D5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D5 - hit")
                D5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D5) VALUES(1)")
        connection.commit()

    if D6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D6')"):
            if row == (0,):
                print("D6 - miss")
                D6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D6 - hit")
                D6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D6) VALUES(1)")
        connection.commit()

    if D7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D7')"):
            if row == (0,):
                print("D7 - miss")
                D7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D7 - hit")
                D7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D7) VALUES(1)")
        connection.commit()

    if D8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D8')"):
            if row == (0,):
                print("D8 - miss")
                D8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D8 - hit")
                D8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D8) VALUES(1)")
        connection.commit()

    if D9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'D9')"):
            if row == (0,):
                print("D9 - miss")
                D9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D9 - hit")
                D9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(D9) VALUES(1)")
        connection.commit()

        
    if E1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E1')"):
            if row == (0,):
                print("E1 - miss")
                E1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E1 - hit")
                E1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E1) VALUES(1)")
        connection.commit()

    if E2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E2')"):
            if row == (0,):
                print("E2 - miss")
                E2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E2 - hit")
                E2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E2) VALUES(1)")
        connection.commit()

    if E3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E3')"):
            if row == (0,):
                print("E3 - miss")
                E3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E3 - hit")
                E3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E3) VALUES(1)")
        connection.commit()

    if E4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E4')"):
            if row == (0,):
                print("E4 - miss")
                E4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E4 - hit")
                E4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E4) VALUES(1)")
        connection.commit()

    if E5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E5')"):
            if row == (0,):
                print("E5 - miss")
                E5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E5 - hit")
                E5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E5) VALUES(1)")
        connection.commit()

    if E6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E6')"):
            if row == (0,):
                print("E6 - miss")
                E6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E6 - hit")
                E6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E6) VALUES(1)")
        connection.commit()

    if E7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E7')"):
            if row == (0,):
                print("E7 - miss")
                E7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E7 - hit")
                E7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E7) VALUES(1)")
        connection.commit()

    if E8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E8')"):
            if row == (0,):
                print("E8 - miss")
                E8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E8 - hit")
                E8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E8) VALUES(1)")
        connection.commit()

    if E9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'E9')"):
            if row == (0,):
                print("E9 - miss")
                E9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E9 - hit")
                E9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(E9) VALUES(1)")
        connection.commit()

        
    if F1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F1')"):
            if row == (0,):
                print("F1 - miss")
                F1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F1 - hit")
                F1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F1) VALUES(1)")
        connection.commit()

    if F2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F2')"):
            if row == (0,):
                print("F2 - miss")
                F2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F2 - hit")
                F2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F2) VALUES(1)")
        connection.commit()

    if F3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F3')"):
            if row == (0,):
                print("F3 - miss")
                F3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F3 - hit")
                F3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F3) VALUES(1)")
        connection.commit()

    if F4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F4')"):
            if row == (0,):
                print("F4 - miss")
                F4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F4 - hit")
                F4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F4) VALUES(1)")
        connection.commit()

    if F5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F5')"):
            if row == (0,):
                print("F5 - miss")
                F5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F5 - hit")
                F5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F5) VALUES(1)")
        connection.commit()

    if F6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F6')"):
            if row == (0,):
                print("F6 - miss")
                F6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F6 - hit")
                F6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F6) VALUES(1)")
        connection.commit()

    if F7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F7')"):
            if row == (0,):
                print("F7 - miss")
                F7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F7 - hit")
                F7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F7) VALUES(1)")
        connection.commit()

    if F8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F8')"):
            if row == (0,):
                print("F8 - miss")
                F8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F8 - hit")
                F8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F8) VALUES(1)")
        connection.commit()

    if F9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'F9')"):
            if row == (0,):
                print("F9 - miss")
                F9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F9 - hit")
                F9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(F9) VALUES(1)")
        connection.commit()

        
    if G1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G1')"):
            if row == (0,):
                print("G1 - miss")
                G1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G1 - hit")
                G1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G1) VALUES(1)")
        connection.commit()

    if G2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G2')"):
            if row == (0,):
                print("G2 - miss")
                G2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G2 - hit")
                G2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G2) VALUES(1)")
        connection.commit()

    if G3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G3')"):
            if row == (0,):
                print("G3 - miss")
                G3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G3 - hit")
                G3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G3) VALUES(1)")
        connection.commit()

    if G4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G4')"):
            if row == (0,):
                print("G4 - miss")
                G4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G4 - hit")
                G4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G4) VALUES(1)")
        connection.commit()

    if G5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G5')"):
            if row == (0,):
                print("G5 - miss")
                G5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G5 - hit")
                G5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G5) VALUES(1)")
        connection.commit()

    if G6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G6')"):
            if row == (0,):
                print("G6 - miss")
                G6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G6 - hit")
                G6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G6) VALUES(1)")
        connection.commit()

    if G7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G7')"):
            if row == (0,):
                print("G7 - miss")
                G7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G7 - hit")
                G7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G7) VALUES(1)")
        connection.commit()

    if G8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G8')"):
            if row == (0,):
                print("G8 - miss")
                G8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G8 - hit")
                G8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G8) VALUES(1)")
        connection.commit()

    if G9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'G9')"):
            if row == (0,):
                print("G9 - miss")
                G9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G9 - hit")
                G9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(G9) VALUES(1)")
        connection.commit()

    
    if H1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H1')"):
            if row == (0,):
                print("H1 - miss")
                H1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H1 - hit")
                H1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H1) VALUES(1)")
        connection.commit()

    if H2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H2')"):
            if row == (0,):
                print("H2 - miss")
                H2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H2 - hit")
                H2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H2) VALUES(1)")
        connection.commit()

    if H3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H3')"):
            if row == (0,):
                print("H3 - miss")
                H3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H3 - hit")
                H3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H3) VALUES(1)")
        connection.commit()

    if H4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H4')"):
            if row == (0,):
                print("H4 - miss")
                H4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H4 - hit")
                H4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H4) VALUES(1)")
        connection.commit()

    if H5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H5')"):
            if row == (0,):
                print("H5 - miss")
                H5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H5 - hit")
                H5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H5) VALUES(1)")
        connection.commit()

    if H6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H6')"):
            if row == (0,):
                print("H6 - miss")
                H6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H6 - hit")
                H6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H6) VALUES(1)")
        connection.commit()

    if H7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H7')"):
            if row == (0,):
                print("H7 - miss")
                H7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H7 - hit")
                H7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H7) VALUES(1)")
        connection.commit()

    if H8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H8')"):
            if row == (0,):
                print("H8 - miss")
                H8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H8 - hit")
                H8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H8) VALUES(1)")
        connection.commit()

    if H9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'H9')"):
            if row == (0,):
                print("H9 - miss")
                H9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H9 - hit")
                H9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(H9) VALUES(1)")
        connection.commit()

        
    if I1Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I1')"):
            if row == (0,):
                print("I1 - miss")
                I1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I1 - hit")
                I1.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I1) VALUES(1)")
        connection.commit()

    if I2Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I2')"):
            if row == (0,):
                print("I2 - miss")
                I2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I2 - hit")
                I2.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I2) VALUES(1)")
        connection.commit()

    if I3Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I3')"):
            if row == (0,):
                print("I3 - miss")
                I3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I3 - hit")
                I3.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I3) VALUES(1)")
        connection.commit()

    if I4Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I4')"):
            if row == (0,):
                print("I4 - miss")
                I4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I4 - hit")
                I4.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I4) VALUES(1)")
        connection.commit()

    if I5Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I5')"):
            if row == (0,):
                print("I5 - miss")
                I5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I5 - hit")
                I5.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I5) VALUES(1)")
        connection.commit()

    if I6Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I6')"):
            if row == (0,):
                print("I6 - miss")
                I6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I6 - hit")
                I6.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I6) VALUES(1)")
        connection.commit()

    if I7Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I7')"):
            if row == (0,):
                print("I7 - miss")
                I7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I7 - hit")
                I7.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I7) VALUES(1)")
        connection.commit()

    if I8Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I8')"):
            if row == (0,):
                print("I8 - miss")
                I8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I8 - hit")
                I8.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I8) VALUES(1)")
        connection.commit()

    if I9Clicked == True:
        for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player2_ships = 'I9')"):
            if row == (0,):
                print("I9 - miss")
                I9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I9 - hit")
                I9.configure(fg="black", bg="red", state=DISABLED)
        
        cursor.execute("INSERT INTO p1_reveals(I9) VALUES(1)")
        connection.commit()


hitlabel = Button(root, text = (p1wincon, " player 2 ship grids hit"), bg="light green", activebackground="light yellow")
hitlabel.grid(row = 12, column = 0, columnspan = 2,)
print(p1wincon , "/17 player 2 ship grids found")

root.mainloop()
