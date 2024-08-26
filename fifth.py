"""tkinter provides the majority of functions for the gui"""
from tkinter import Tk, Frame, CENTER, Button, Label, DISABLED, messagebox
import subprocess
import sqlite3
from PIL import ImageTk, Image


root = Tk()
root.title("PLAYER 1 GUESS PLAYER 2 SHIP PLACEMENTS")

root.tk.call('wm', 'iconphoto', root, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.geometry("900x600")
root.configure(background="light green")


connection = sqlite3.connect("battleships.db")
cursor =connection.cursor()


cursor.execute("""create table if not exists board_details
                (player1_ships text, player2_ships text, player1_guess text, player2_guess text)""")
connection.commit()

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
    """Function drops tables and quits game"""
    cursor.execute("DROP TABLE board_details")
    cursor.execute("DROP TABLE p1_reveals")
    cursor.execute("DROP TABLE p2_reveals")
    messagebox.showinfo("BATTLESHIPS", "killing game")
    root.quit()

button_exit=Button(board3, text="Exit Program",
                    bg="yellow", activebackground="red", activeforeground="white",
                    command = gamequit)
button_exit.grid(row=9, column=9)


def p1guessing():
    """Function checks if player 1's guess is valid to progress to player 2's guess"""
    if P1GUESS_COUNT < 1:
        messagebox.showinfo("!!!PLAYER 1!!!","GUESS 1 SHIP FROM PLAYER 2 BEFORE CONFIRMATION")

    else:
        guesscheck()
        cursor.execute("UPDATE board_details SET player1_guess = NULL")
        cursor.execute("""DELETE FROM board_details WHERE
                       player1_ships IS NULL AND player2_ships IS NULL AND player1_guess IS NULL""")
        connection.commit()
        messagebox.showinfo("PLAYER 1 GUESSED A SHIP POSITION",
                            "NOW PLAYER 2 GETS TO GUESS ONE OF YOUR SHIP LOCATIONS")
        root.destroy()
        subprocess.run(["python", ("sixth.py")], check=False)


def p1resetguess():
    """Function allows player to change their ship guess"""
    cursor.execute("UPDATE board_details SET player1_guess = NULL")
    cursor.execute("""DELETE FROM board_details WHERE
                   player1_ships IS NULL AND player2_ships IS NULL AND player1_guess IS NULL""")
    connection.commit()
    messagebox.showinfo("PLAYER 1 BOARD", "PLAYER 2 SHIP GUESS RESET")
    root.destroy()
    subprocess.run(["python", ("fifth.py")], check=False)


p1_con_place = Button(root, text="CONFIRM GUESS", padx = 10, pady = 5,
                    fg="orange", bg="black", activebackground="orange", activeforeground="black",
                    command = p1guessing)
p1_con_place.grid()

p1_res_place = Button(root, text="reset guess", padx = 10, pady = 5,
                    fg="orange", bg="black", activebackground="orange", activeforeground="black",
                    command = p1resetguess)
p1_res_place.grid()


def p1winning():
    """Function to end the game, when one player finds all the others ships"""
    messagebox.showinfo("PLAYER 1 WINS", "player 1 hit all of player 2's ships")
    gamequit()

#Define global guess count.
P1GUESS_COUNT = 0
P1WIN_CON = 0

playerlabel = Label(text="PLAYER 1:", bg="light green")
playerlabel.grid(row=7, column=0)

#count display
countlabel = Button(root, text = "guess an enemy ship location",
                    bg="light green", activebackground="light yellow")
countlabel.grid(row = 9, column = 0, columnspan = 2,)

limitlabel = Label(text="(you only get one guess)", bg="light green")
limitlabel.grid(row=10, column=0)


# Before first click
A1CLICKED  = False
A2CLICKED  = False
A3CLICKED  = False
A4CLICKED  = False
A5CLICKED  = False
A6CLICKED  = False
A7CLICKED  = False
A8CLICKED  = False
A9CLICKED  = False

B1CLICKED  = False
B2CLICKED  = False
B3CLICKED  = False
B4CLICKED  = False
B5CLICKED  = False
B6CLICKED  = False
B7CLICKED  = False
B8CLICKED  = False
B9CLICKED  = False

C1CLICKED  = False
C2CLICKED  = False
C3CLICKED  = False
C4CLICKED  = False
C5CLICKED  = False
C6CLICKED  = False
C7CLICKED  = False
C8CLICKED  = False
C9CLICKED  = False

D1CLICKED  = False
D2CLICKED  = False
D3CLICKED  = False
D4CLICKED  = False
D5CLICKED  = False
D6CLICKED  = False
D7CLICKED  = False
D8CLICKED  = False
D9CLICKED  = False

E1CLICKED  = False
E2CLICKED  = False
E3CLICKED  = False
E4CLICKED  = False
E5CLICKED  = False
E6CLICKED  = False
E7CLICKED  = False
E8CLICKED  = False
E9CLICKED  = False

F1CLICKED  = False
F2CLICKED  = False
F3CLICKED  = False
F4CLICKED  = False
F5CLICKED  = False
F6CLICKED  = False
F7CLICKED  = False
F8CLICKED  = False
F9CLICKED  = False

G1CLICKED  = False
G2CLICKED  = False
G3CLICKED  = False
G4CLICKED  = False
G5CLICKED  = False
G6CLICKED  = False
G7CLICKED  = False
G8CLICKED  = False
G9CLICKED  = False

H1CLICKED  = False
H2CLICKED  = False
H3CLICKED  = False
H4CLICKED  = False
H5CLICKED  = False
H6CLICKED  = False
H7CLICKED  = False
H8CLICKED  = False
H9CLICKED  = False

I1CLICKED  = False
I2CLICKED  = False
I3CLICKED  = False
I4CLICKED  = False
I5CLICKED  = False
I6CLICKED  = False
I7CLICKED  = False
I8CLICKED  = False
I9CLICKED  = False


def guesslimit():
    """Function locks board buttons that haven't been clicked, when guess limit is hit""" 
    if A1CLICKED is False:
        A1.configure(fg="black", bg="white", state=DISABLED)
    if A2CLICKED is False:
        A2.configure(fg="black", bg="white", state=DISABLED)
    if A3CLICKED is False:
        A3.configure(fg="black", bg="white", state=DISABLED)
    if A4CLICKED is False:
        A4.configure(fg="black", bg="white", state=DISABLED)
    if A5CLICKED is False:
        A5.configure(fg="black", bg="white", state=DISABLED)
    if A6CLICKED is False:
        A6.configure(fg="black", bg="white", state=DISABLED)
    if A7CLICKED is False:
        A7.configure(fg="black", bg="white", state=DISABLED)
    if A8CLICKED is False:
        A8.configure(fg="black", bg="white", state=DISABLED)
    if A9CLICKED is False:
        A9.configure(fg="black", bg="white", state=DISABLED)

    if B1CLICKED is False:
        B1.configure(fg="black", bg="white", state=DISABLED)
    if B2CLICKED is False:
        B2.configure(fg="black", bg="white", state=DISABLED)
    if B3CLICKED is False:
        B3.configure(fg="black", bg="white", state=DISABLED)
    if B4CLICKED is False:
        B4.configure(fg="black", bg="white", state=DISABLED)
    if B5CLICKED is False:
        B5.configure(fg="black", bg="white", state=DISABLED)
    if B6CLICKED is False:
        B6.configure(fg="black", bg="white", state=DISABLED)
    if B7CLICKED is False:
        B7.configure(fg="black", bg="white", state=DISABLED)
    if B8CLICKED is False:
        B8.configure(fg="black", bg="white", state=DISABLED)
    if B9CLICKED is False:
        B9.configure(fg="black", bg="white", state=DISABLED)

    if C1CLICKED is False:
        C1.configure(fg="black", bg="white", state=DISABLED)
    if C2CLICKED is False:
        C2.configure(fg="black", bg="white", state=DISABLED)
    if C3CLICKED is False:
        C3.configure(fg="black", bg="white", state=DISABLED)
    if C4CLICKED is False:
        C4.configure(fg="black", bg="white", state=DISABLED)
    if C5CLICKED is False:
        C5.configure(fg="black", bg="white", state=DISABLED)
    if C6CLICKED is False:
        C6.configure(fg="black", bg="white", state=DISABLED)
    if C7CLICKED is False:
        C7.configure(fg="black", bg="white", state=DISABLED)
    if C8CLICKED is False:
        C8.configure(fg="black", bg="white", state=DISABLED)
    if C9CLICKED is False:
        C9.configure(fg="black", bg="white", state=DISABLED)

    if D1CLICKED is False:
        D1.configure(fg="black", bg="white", state=DISABLED)
    if D2CLICKED is False:
        D2.configure(fg="black", bg="white", state=DISABLED)
    if D3CLICKED is False:
        D3.configure(fg="black", bg="white", state=DISABLED)
    if D4CLICKED is False:
        D4.configure(fg="black", bg="white", state=DISABLED)
    if D5CLICKED is False:
        D5.configure(fg="black", bg="white", state=DISABLED)
    if D6CLICKED is False:
        D6.configure(fg="black", bg="white", state=DISABLED)
    if D7CLICKED is False:
        D7.configure(fg="black", bg="white", state=DISABLED)
    if D8CLICKED is False:
        D8.configure(fg="black", bg="white", state=DISABLED)
    if D9CLICKED is False:
        D9.configure(fg="black", bg="white", state=DISABLED)

    if E1CLICKED is False:
        E1.configure(fg="black", bg="white", state=DISABLED)
    if E2CLICKED is False:
        E2.configure(fg="black", bg="white", state=DISABLED)
    if E3CLICKED is False:
        E3.configure(fg="black", bg="white", state=DISABLED)
    if E4CLICKED is False:
        E4.configure(fg="black", bg="white", state=DISABLED)
    if E5CLICKED is False:
        E5.configure(fg="black", bg="white", state=DISABLED)
    if E6CLICKED is False:
        E6.configure(fg="black", bg="white", state=DISABLED)
    if E7CLICKED is False:
        E7.configure(fg="black", bg="white", state=DISABLED)
    if E8CLICKED is False:
        E8.configure(fg="black", bg="white", state=DISABLED)
    if E9CLICKED is False:
        E9.configure(fg="black", bg="white", state=DISABLED)

    if F1CLICKED is False:
        F1.configure(fg="black", bg="white", state=DISABLED)
    if F2CLICKED is False:
        F2.configure(fg="black", bg="white", state=DISABLED)
    if F3CLICKED is False:
        F3.configure(fg="black", bg="white", state=DISABLED)
    if F4CLICKED is False:
        F4.configure(fg="black", bg="white", state=DISABLED)
    if F5CLICKED is False:
        F5.configure(fg="black", bg="white", state=DISABLED)
    if F6CLICKED is False:
        F6.configure(fg="black", bg="white", state=DISABLED)
    if F7CLICKED is False:
        F7.configure(fg="black", bg="white", state=DISABLED)
    if F8CLICKED is False:
        F8.configure(fg="black", bg="white", state=DISABLED)
    if F9CLICKED is False:
        F9.configure(fg="black", bg="white", state=DISABLED)

    if G1CLICKED is False:
        G1.configure(fg="black", bg="white", state=DISABLED)
    if G2CLICKED is False:
        G2.configure(fg="black", bg="white", state=DISABLED)
    if G3CLICKED is False:
        G3.configure(fg="black", bg="white", state=DISABLED)
    if G4CLICKED is False:
        G4.configure(fg="black", bg="white", state=DISABLED)
    if G5CLICKED is False:
        G5.configure(fg="black", bg="white", state=DISABLED)
    if G6CLICKED is False:
        G6.configure(fg="black", bg="white", state=DISABLED)
    if G7CLICKED is False:
        G7.configure(fg="black", bg="white", state=DISABLED)
    if G8CLICKED is False:
        G8.configure(fg="black", bg="white", state=DISABLED)
    if G9CLICKED is False:
        G9.configure(fg="black", bg="white", state=DISABLED)

    if H1CLICKED is False:
        H1.configure(fg="black", bg="white", state=DISABLED)
    if H2CLICKED is False:
        H2.configure(fg="black", bg="white", state=DISABLED)
    if H3CLICKED is False:
        H3.configure(fg="black", bg="white", state=DISABLED)
    if H4CLICKED is False:
        H4.configure(fg="black", bg="white", state=DISABLED)
    if H5CLICKED is False:
        H5.configure(fg="black", bg="white", state=DISABLED)
    if H6CLICKED is False:
        H6.configure(fg="black", bg="white", state=DISABLED)
    if H7CLICKED is False:
        H7.configure(fg="black", bg="white", state=DISABLED)
    if H8CLICKED is False:
        H8.configure(fg="black", bg="white", state=DISABLED)
    if H9CLICKED is False:
        H9.configure(fg="black", bg="white", state=DISABLED)

    if I1CLICKED is False:
        I1.configure(fg="black", bg="white", state=DISABLED)
    if I2CLICKED is False:
        I2.configure(fg="black", bg="white", state=DISABLED)
    if I3CLICKED is False:
        I3.configure(fg="black", bg="white", state=DISABLED)
    if I4CLICKED is False:
        I4.configure(fg="black", bg="white", state=DISABLED)
    if I5CLICKED is False:
        I5.configure(fg="black", bg="white", state=DISABLED)
    if I6CLICKED is False:
        I6.configure(fg="black", bg="white", state=DISABLED)
    if I7CLICKED is False:
        I7.configure(fg="black", bg="white", state=DISABLED)
    if I8CLICKED is False:
        I8.configure(fg="black", bg="white", state=DISABLED)
    if I9CLICKED is False:
        I9.configure(fg="black", bg="white", state=DISABLED)


def xay1():
    """Function for the grid coordinate"""
    global A1CLICKED
    A1CLICKED = not A1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grid guessed"))
    print(P1GUESS_COUNT , " ship grid guessed")

    A1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()


def xay2():
    """Function for the grid coordinate"""
    global A2CLICKED
    A2CLICKED = not A2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay3():
    """Function for the grid coordinate"""
    global A3CLICKED
    A3CLICKED = not A3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay4():
    """Function for the grid coordinate"""
    global A4CLICKED
    A4CLICKED = not A4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay5():
    """Function for the grid coordinate"""
    global A5CLICKED
    A5CLICKED = not A5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay6():
    """Function for the grid coordinate"""
    global A6CLICKED
    A6CLICKED = not A6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay7():
    """Function for the grid coordinate"""
    global A7CLICKED
    A7CLICKED = not A7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay8():
    """Function for the grid coordinate"""
    global A8CLICKED
    A8CLICKED = not A8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xay9():
    """Function for the grid coordinate"""
    global A9CLICKED
    A9CLICKED = not A9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('A9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    A9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()



def xby1():
    """Function for the grid coordinate"""
    global B1CLICKED
    B1CLICKED = not B1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby2():
    """Function for the grid coordinate"""
    global B2CLICKED
    B2CLICKED = not B2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby3():
    """Function for the grid coordinate"""
    global B3CLICKED
    B3CLICKED = not B3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby4():
    """Function for the grid coordinate"""
    global B4CLICKED
    B4CLICKED = not B4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby5():
    """Function for the grid coordinate"""
    global B5CLICKED
    B5CLICKED = not B5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby6():
    """Function for the grid coordinate"""
    global B6CLICKED
    B6CLICKED = not B6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby7():
    """Function for the grid coordinate"""
    global B7CLICKED
    B7CLICKED = not B7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby8():
    """Function for the grid coordinate"""
    global B8CLICKED
    B8CLICKED = not B8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xby9():
    """Function for the grid coordinate"""
    global B9CLICKED
    B9CLICKED = not B9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('B9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    B9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()



def xcy1():
    """Function for the grid coordinate"""
    global C1CLICKED
    C1CLICKED = not C1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy2():
    """Function for the grid coordinate"""
    global C2CLICKED
    C2CLICKED = not C2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy3():
    """Function for the grid coordinate"""
    global C3CLICKED
    C3CLICKED = not C3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy4():
    """Function for the grid coordinate"""
    global C4CLICKED
    C4CLICKED = not C4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy5():
    """Function for the grid coordinate"""
    global C5CLICKED
    C5CLICKED = not C5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy6():
    """Function for the grid coordinate"""
    global C6CLICKED
    C6CLICKED = not C6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy7():
    """Function for the grid coordinate"""
    global C7CLICKED
    C7CLICKED = not C7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy8():
    """Function for the grid coordinate"""
    global C8CLICKED
    C8CLICKED = not C8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xcy9():
    """Function for the grid coordinate"""
    global C9CLICKED
    C9CLICKED = not C9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('C9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    C9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()



def xdy1():
    """Function for the grid coordinate"""
    global D1CLICKED
    D1CLICKED = not D1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy2():
    """Function for the grid coordinate"""
    global D2CLICKED
    D2CLICKED = not D2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy3():
    """Function for the grid coordinate"""
    global D3CLICKED
    D3CLICKED = not D3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy4():
    """Function for the grid coordinate"""
    global D4CLICKED
    D4CLICKED = not D4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy5():
    """Function for the grid coordinate"""
    global D5CLICKED
    D5CLICKED = not D5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy6():
    """Function for the grid coordinate"""
    global D6CLICKED
    D6CLICKED = not D6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy7():
    """Function for the grid coordinate"""
    global D7CLICKED
    D7CLICKED = not D7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy8():
    """Function for the grid coordinate"""
    global D8CLICKED
    D8CLICKED = not D8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xdy9():
    """Function for the grid coordinate"""
    global D9CLICKED
    D9CLICKED = not D9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('D9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    D9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()



def xey1():
    """Function for the grid coordinate"""
    global E1CLICKED
    E1CLICKED = not E1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey2():
    """Function for the grid coordinate"""
    global E2CLICKED
    E2CLICKED = not E2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey3():
    """Function for the grid coordinate"""
    global E3CLICKED
    E3CLICKED = not E3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey4():
    """Function for the grid coordinate"""
    global E4CLICKED
    E4CLICKED = not E4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey5():
    """Function for the grid coordinate"""
    global E5CLICKED
    E5CLICKED = not E5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey6():
    """Function for the grid coordinate"""
    global E6CLICKED
    E6CLICKED = not E6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey7():
    """Function for the grid coordinate"""
    global E7CLICKED
    E7CLICKED = not E7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey8():
    """Function for the grid coordinate"""
    global E8CLICKED
    E8CLICKED = not E8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xey9():
    """Function for the grid coordinate"""
    global E9CLICKED
    E9CLICKED = not E9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('E9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    E9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()




def xfy1():
    """Function for the grid coordinate"""
    global F1CLICKED
    F1CLICKED = not F1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy2():
    """Function for the grid coordinate"""
    global F2CLICKED
    F2CLICKED = not F2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy3():
    """Function for the grid coordinate"""
    global F3CLICKED
    F3CLICKED = not F3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy4():
    """Function for the grid coordinate"""
    global F4CLICKED
    F4CLICKED = not F4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy5():
    """Function for the grid coordinate"""
    global F5CLICKED
    F5CLICKED = not F5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy6():
    """Function for the grid coordinate"""
    global F6CLICKED
    F6CLICKED = not F6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy7():
    """Function for the grid coordinate"""
    global F7CLICKED
    F7CLICKED = not F7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy8():
    """Function for the grid coordinate"""
    global F8CLICKED
    F8CLICKED = not F8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xfy9():
    """Function for the grid coordinate"""
    global F9CLICKED
    F9CLICKED = not F9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('F9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    F9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()




def xgy1():
    """Function for the grid coordinate"""
    global G1CLICKED
    G1CLICKED = not G1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy2():
    """Function for the grid coordinate"""
    global G2CLICKED
    G2CLICKED = not G2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy3():
    """Function for the grid coordinate"""
    global G3CLICKED
    G3CLICKED = not G3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy4():
    """Function for the grid coordinate"""
    global G4CLICKED
    G4CLICKED = not G4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy5():
    """Function for the grid coordinate"""
    global G5CLICKED
    G5CLICKED = not G5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy6():
    """Function for the grid coordinate"""
    global G6CLICKED
    G6CLICKED = not G6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy7():
    """Function for the grid coordinate"""
    global G7CLICKED
    G7CLICKED = not G7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy8():
    """Function for the grid coordinate"""
    global G8CLICKED
    G8CLICKED = not G8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xgy9():
    """Function for the grid coordinate"""
    global G9CLICKED
    G9CLICKED = not G9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('G9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    G9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()




def xhy1():
    """Function for the grid coordinate"""
    global H1CLICKED
    H1CLICKED = not H1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy2():
    """Function for the grid coordinate"""
    global H2CLICKED
    H2CLICKED = not H2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy3():
    """Function for the grid coordinate"""
    global H3CLICKED
    H3CLICKED = not H3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy4():
    """Function for the grid coordinate"""
    global H4CLICKED
    H4CLICKED = not H4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy5():
    """Function for the grid coordinate"""
    global H5CLICKED
    H5CLICKED = not H5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy6():
    """Function for the grid coordinate"""
    global H6CLICKED
    H6CLICKED = not H6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy7():
    """Function for the grid coordinate"""
    global H7CLICKED
    H7CLICKED = not H7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy8():
    """Function for the grid coordinate"""
    global H8CLICKED
    H8CLICKED = not H8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xhy9():
    """Function for the grid coordinate"""
    global H9CLICKED
    H9CLICKED = not H9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('H9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    H9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()




def xiy1():
    """Function for the grid coordinate"""
    global I1CLICKED
    I1CLICKED = not I1CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I1.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy2():
    """Function for the grid coordinate"""
    global I2CLICKED
    I2CLICKED = not I2CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I2.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy3():
    """Function for the grid coordinate"""
    global I3CLICKED
    I3CLICKED = not I3CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I3.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy4():
    """Function for the grid coordinate"""
    global I4CLICKED
    I4CLICKED = not I4CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I4.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy5():
    """Function for the grid coordinate"""
    global I5CLICKED
    I5CLICKED = not I5CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I5.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy6():
    """Function for the grid coordinate"""
    global I6CLICKED
    I6CLICKED = not I6CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I6.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy7():
    """Function for the grid coordinate"""
    global I7CLICKED
    I7CLICKED = not I7CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I7.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy8():
    """Function for the grid coordinate"""
    global I8CLICKED
    I8CLICKED = not I8CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I8.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()

def xiy9():
    """Function for the grid coordinate"""
    global I9CLICKED
    I9CLICKED = not I9CLICKED

    cursor.execute("INSERT INTO board_details(player1_guess) VALUES('I9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P1GUESS_COUNT
    P1GUESS_COUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1GUESS_COUNT, " ship grids chosen"))
    print(P1GUESS_COUNT , " ship grids placed")


    I9.configure(fg="black", bg="green", state=DISABLED)

    if P1GUESS_COUNT >= 1:
        guesslimit()



A1 = Button(board3, text="A1", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xay1,)
A2 = Button(board3, text="A2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay2)
A3 = Button(board3, text="A3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay3)
A4 = Button(board3, text="A4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay4)
A5 = Button(board3, text="A5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay5)
A6 = Button(board3, text="A6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay6)
A7 = Button(board3, text="A7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay7)
A8 = Button(board3, text="A8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay8)
A9 = Button(board3, text="A9", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xay9)


B1 = Button(board3, text="B1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby1)
B2 = Button(board3, text="B2", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby2)
B3 = Button(board3, text="B3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby3)
B4 = Button(board3, text="B4", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby4)
B5 = Button(board3, text="B5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby5)
B6 = Button(board3, text="B6", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby6)
B7 = Button(board3, text="B7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby7)
B8 = Button(board3, text="B8", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby8)
B9 = Button(board3, text="B9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby9)


C1 = Button(board3, text="C1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy1)
C2 = Button(board3, text="C2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy2)
C3 = Button(board3, text="C3", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xcy3)
C4 = Button(board3, text="C4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy4)
C5 = Button(board3, text="C5", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xcy5)
C6 = Button(board3, text="C6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy6)
C7 = Button(board3, text="C7", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xcy7)
C8 = Button(board3, text="C8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy8)
C9 = Button(board3, text="C9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy9)


D1 = Button(board3, text="D1", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xdy1)
D2 = Button(board3, text="D2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy2)
D3 = Button(board3, text="D3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy3)
D4 = Button(board3, text="D4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy4)
D5 = Button(board3, text="D5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy5)
D6 = Button(board3, text="D6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy6)
D7 = Button(board3, text="D7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy7)
D8 = Button(board3, text="D8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy8)
D9 = Button(board3, text="D9", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xdy9)


E1 = Button(board3, text="E1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey1)
E2 = Button(board3, text="E2", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey2)
E3 = Button(board3, text="E3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey3)
E4 = Button(board3, text="E4", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey4)
E5 = Button(board3, text="E5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey5)
E6 = Button(board3, text="E6", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey6)
E7 = Button(board3, text="E7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey7)
E8 = Button(board3, text="E8", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey8)
E9 = Button(board3, text="E9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey9)


F1 = Button(board3, text="F1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy1)
F2 = Button(board3, text="F2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy2)
F3 = Button(board3, text="F3", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xfy3)
F4 = Button(board3, text="F4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy4)
F5 = Button(board3, text="F5", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xfy5)
F6 = Button(board3, text="F6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy6)
F7 = Button(board3, text="F7", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xfy7)
F8 = Button(board3, text="F8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy8)
F9 = Button(board3, text="F9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy9)


G1 = Button(board3, text="G1", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xgy1)
G2 = Button(board3, text="G2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy2)
G3 = Button(board3, text="G3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy3)
G4 = Button(board3, text="G4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy4)
G5 = Button(board3, text="G5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy5)
G6 = Button(board3, text="G6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy6)
G7 = Button(board3, text="G7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy7)
G8 = Button(board3, text="G8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy8)
G9 = Button(board3, text="G9", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xgy9)


H1 = Button(board3, text="H1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy1)
H2 = Button(board3, text="H2", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy2)
H3 = Button(board3, text="H3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy3)
H4 = Button(board3, text="H4", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy4)
H5 = Button(board3, text="H5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy5)
H6 = Button(board3, text="H6", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy6)
H7 = Button(board3, text="H7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy7)
H8 = Button(board3, text="H8", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy8)
H9 = Button(board3, text="H9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy9)


I1 = Button(board3, text="I1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy1)
I2 = Button(board3, text="I2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy2)
I3 = Button(board3, text="I3", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xiy3)
I4 = Button(board3, text="I4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy4)
I5 = Button(board3, text="I5", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xiy5)
I6 = Button(board3, text="I6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy6)
I7 = Button(board3, text="I7", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xiy7)
I8 = Button(board3, text="I8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy8)
I9 = Button(board3, text="I9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy9)


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
    """Function to check if a grid has been guessed, and if it has, check if it's a hit or a miss"""
    global P1WIN_CON
    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A1')"""):
                if row == (0,):
                    print("A1 - miss")
                    A1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A1 - hit")
                    A1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A2')"""):
                if row == (0,):
                    print("A2 - miss")
                    A2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A2 - hit")
                    A2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A3')"""):
                if row == (0,):
                    print("A3 - miss")
                    A3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A3 - hit")
                    A3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A4')"""):
                if row == (0,):
                    print("A4 - miss")
                    A4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A4 - hit")
                    A4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A5')"""):
                if row == (0,):
                    print("A5 - miss")
                    A5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A5 - hit")
                    A5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A6')"""):
                if row == (0,):
                    print("A6 - miss")
                    A6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A6 - hit")
                    A6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A7')"""):
                if row == (0,):
                    print("A7 - miss")
                    A7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A7 - hit")
                    A7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A8')"""):
                if row == (0,):
                    print("A8 - miss")
                    A8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A8 - hit")
                    A8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE A9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'A9')"""):
                if row == (0,):
                    print("A9 - miss")
                    A9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("A9 - hit")
                    A9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B1')"""):
                if row == (0,):
                    print("B1 - miss")
                    B1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B1 - hit")
                    B1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B2')"""):
                if row == (0,):
                    print("B2 - miss")
                    B2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B2 - hit")
                    B2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B3')"""):
                if row == (0,):
                    print("B3 - miss")
                    B3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B3 - hit")
                    B3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B4')"""):
                if row == (0,):
                    print("B4 - miss")
                    B4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B4 - hit")
                    B4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B5')"""):
                if row == (0,):
                    print("B5 - miss")
                    B5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B5 - hit")
                    B5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B6')"""):
                if row == (0,):
                    print("B6 - miss")
                    B6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B6 - hit")
                    B6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B7')"""):
                if row == (0,):
                    print("B7 - miss")
                    B7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B7 - hit")
                    B7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B8')"""):
                if row == (0,):
                    print("B8 - miss")
                    B8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B8 - hit")
                    B8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE B9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'B9')"""):
                if row == (0,):
                    print("B9 - miss")
                    B9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("B9 - hit")
                    B9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C1')"""):
                if row == (0,):
                    print("C1 - miss")
                    C1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C1 - hit")
                    C1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C2')"""):
                if row == (0,):
                    print("C2 - miss")
                    C2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C2 - hit")
                    C2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C3')"""):
                if row == (0,):
                    print("C3 - miss")
                    C3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C3 - hit")
                    C3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C4')"""):
                if row == (0,):
                    print("C4 - miss")
                    C4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C4 - hit")
                    C4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C5')"""):
                if row == (0,):
                    print("C5 - miss")
                    C5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C5 - hit")
                    C5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C6')"""):
                if row == (0,):
                    print("C6 - miss")
                    C6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C6 - hit")
                    C6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C7')"""):
                if row == (0,):
                    print("C7 - miss")
                    C7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C7 - hit")
                    C7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C8')"""):
                if row == (0,):
                    print("C8 - miss")
                    C8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C8 - hit")
                    C8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE C9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'C9')"""):
                if row == (0,):
                    print("C9 - miss")
                    C9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("C9 - hit")
                    C9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D1')"""):
                if row == (0,):
                    print("D1 - miss")
                    D1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D1 - hit")
                    D1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D2')"""):
                if row == (0,):
                    print("D2 - miss")
                    D2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D2 - hit")
                    D2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D3')"""):
                if row == (0,):
                    print("D3 - miss")
                    D3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D3 - hit")
                    D3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D4')"""):
                if row == (0,):
                    print("D4 - miss")
                    D4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D4 - hit")
                    D4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D5')"""):
                if row == (0,):
                    print("D5 - miss")
                    D5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D5 - hit")
                    D5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D6')"""):
                if row == (0,):
                    print("D6 - miss")
                    D6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D6 - hit")
                    D6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D7')"""):
                if row == (0,):
                    print("D7 - miss")
                    D7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D7 - hit")
                    D7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D8')"""):
                if row == (0,):
                    print("D8 - miss")
                    D8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D8 - hit")
                    D8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE D9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'D9')"""):
                if row == (0,):
                    print("D9 - miss")
                    D9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("D9 - hit")
                    D9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E1')"""):
                if row == (0,):
                    print("E1 - miss")
                    E1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E1 - hit")
                    E1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E2')"""):
                if row == (0,):
                    print("E2 - miss")
                    E2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E2 - hit")
                    E2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E3')"""):
                if row == (0,):
                    print("E3 - miss")
                    E3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E3 - hit")
                    E3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E4')"""):
                if row == (0,):
                    print("E4 - miss")
                    E4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E4 - hit")
                    E4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E5')"""):
                if row == (0,):
                    print("E5 - miss")
                    E5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E5 - hit")
                    E5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E6')"""):
                if row == (0,):
                    print("E6 - miss")
                    E6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E6 - hit")
                    E6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E7')"""):
                if row == (0,):
                    print("E7 - miss")
                    E7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E7 - hit")
                    E7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E8')"""):
                if row == (0,):
                    print("E8 - miss")
                    E8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E8 - hit")
                    E8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE E9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'E9')"""):
                if row == (0,):
                    print("E9 - miss")
                    E9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("E9 - hit")
                    E9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F1')"""):
                if row == (0,):
                    print("F1 - miss")
                    F1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F1 - hit")
                    F1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F2')"""):
                if row == (0,):
                    print("F2 - miss")
                    F2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F2 - hit")
                    F2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F3')"""):
                if row == (0,):
                    print("F3 - miss")
                    F3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F3 - hit")
                    F3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F4')"""):
                if row == (0,):
                    print("F4 - miss")
                    F4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F4 - hit")
                    F4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F5')"""):
                if row == (0,):
                    print("F5 - miss")
                    F5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F5 - hit")
                    F5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F6')"""):
                if row == (0,):
                    print("F6 - miss")
                    F6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F6 - hit")
                    F6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F7')"""):
                if row == (0,):
                    print("F7 - miss")
                    F7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F7 - hit")
                    F7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F8')"""):
                if row == (0,):
                    print("F8 - miss")
                    F8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F8 - hit")
                    F8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE F9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'F9')"""):
                if row == (0,):
                    print("F9 - miss")
                    F9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("F9 - hit")
                    F9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G1')"""):
                if row == (0,):
                    print("G1 - miss")
                    G1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G1 - hit")
                    G1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G2')"""):
                if row == (0,):
                    print("G2 - miss")
                    G2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G2 - hit")
                    G2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G3')"""):
                if row == (0,):
                    print("G3 - miss")
                    G3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G3 - hit")
                    G3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G4')"""):
                if row == (0,):
                    print("G4 - miss")
                    G4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G4 - hit")
                    G4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G5')"""):
                if row == (0,):
                    print("G5 - miss")
                    G5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G5 - hit")
                    G5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G6')"""):
                if row == (0,):
                    print("G6 - miss")
                    G6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G6 - hit")
                    G6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G7')"""):
                if row == (0,):
                    print("G7 - miss")
                    G7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G7 - hit")
                    G7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G8')"""):
                if row == (0,):
                    print("G8 - miss")
                    G8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G8 - hit")
                    G8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE G9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'G9')"""):
                if row == (0,):
                    print("G9 - miss")
                    G9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("G9 - hit")
                    G9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H1')"""):
                if row == (0,):
                    print("H1 - miss")
                    H1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H1 - hit")
                    H1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H2')"""):
                if row == (0,):
                    print("H2 - miss")
                    H2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H2 - hit")
                    H2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H3')"""):
                if row == (0,):
                    print("H3 - miss")
                    H3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H3 - hit")
                    H3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H4')"""):
                if row == (0,):
                    print("H4 - miss")
                    H4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H4 - hit")
                    H4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H5')"""):
                if row == (0,):
                    print("H5 - miss")
                    H5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H5 - hit")
                    H5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H6')"""):
                if row == (0,):
                    print("H6 - miss")
                    H6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H6 - hit")
                    H6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H7')"""):
                if row == (0,):
                    print("H7 - miss")
                    H7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H7 - hit")
                    H7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H8')"""):
                if row == (0,):
                    print("H8 - miss")
                    H8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H8 - hit")
                    H8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE H9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'H9')"""):
                if row == (0,):
                    print("H9 - miss")
                    H9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("H9 - hit")
                    H9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I1 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I1')"""):
                if row == (0,):
                    print("I1 - miss")
                    I1.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I1 - hit")
                    I1.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I2 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I2')"""):
                if row == (0,):
                    print("I2 - miss")
                    I2.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I2 - hit")
                    I2.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I3 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I3')"""):
                if row == (0,):
                    print("I3 - miss")
                    I3.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I3 - hit")
                    I3.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I4 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I4')"""):
                if row == (0,):
                    print("I4 - miss")
                    I4.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I4 - hit")
                    I4.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I5 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I5')"""):
                if row == (0,):
                    print("I5 - miss")
                    I5.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I5 - hit")
                    I5.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I6 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I6')"""):
                if row == (0,):
                    print("I6 - miss")
                    I6.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I6 - hit")
                    I6.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I7 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I7')"""):
                if row == (0,):
                    print("I7 - miss")
                    I7.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I7 - hit")
                    I7.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I8 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I8')"""):
                if row == (0,):
                    print("I8 - miss")
                    I8.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I8 - hit")
                    I8.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()

    for row in cursor.execute("SELECT EXISTS(select * from p1_reveals WHERE I9 = '1')"):
        if row == (1,):
            for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                      WHERE player2_ships = 'I9')"""):
                if row == (0,):
                    print("I9 - miss")
                    I9.configure(fg="black", bg="white", state=DISABLED)

                if row == (1,):
                    print("I9 - hit")
                    I9.configure(fg="black", bg="red", state=DISABLED)

                    P1WIN_CON += 1  # Update value of global variable.
                    print(P1WIN_CON , "/17 player 2 ship grids found")
                    if P1WIN_CON >= 17:
                        p1winning()


    connection.commit()


ship_history()




#cursor.execute("create table if not exists p1_reveals(A1 bool, A2 bool, A3 bool, A4 bool, A5 bool, A6 bool, A7 bool, A8 bool, A9 bool)")




# cursor.execute("SELECT * FROM board_details WHERE player1_ships = '{}' and player2_guess = '{}'".format(A1CLICKED))

# for row in cursor.execute("select * from board_details "): print(row)

# connection.commit()

def guesscheck():
    """Function for when player submits their guess"""
    if A1CLICKED is True:
        #cursor.execute("SELECT EXISTS(SELECT * FROM board_details WHERE player1_ships = 'A1' and player2_guess = 'A1')")

# for row in cursor.execute("SELECT EXISTS(select * from board_details WHERE player1_ships = 'A1' and player2_guess = 'A1')"):
# if row == (0,):
#     print("miss")
# if row == (1,):
#     print("hit")

        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A1')"""):
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

    if A2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A2')"""):
            if row == (0,):
                print("A2 - miss")
                A2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A2 - hit")
                A2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A2) VALUES(1)")
        connection.commit()

    if A3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A3')"""):
            if row == (0,):
                print("A3 - miss")
                A3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A3 - hit")
                A3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A3) VALUES(1)")
        connection.commit()

    if A4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A4')"""):
            if row == (0,):
                print("A4 - miss")
                A4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A4 - hit")
                A4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A4) VALUES(1)")
        connection.commit()

    if A5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A5')"""):
            if row == (0,):
                print("A5 - miss")
                A5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A5 - hit")
                A5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A5) VALUES(1)")
        connection.commit()

    if A6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A6')"""):
            if row == (0,):
                print("A6 - miss")
                A6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A6 - hit")
                A6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A6) VALUES(1)")
        connection.commit()

    if A7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A7')"""):
            if row == (0,):
                print("A7 - miss")
                A7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A7 - hit")
                A7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A7) VALUES(1)")
        connection.commit()

    if A8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A8')"""):
            if row == (0,):
                print("A8 - miss")
                A8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A8 - hit")
                A8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A8) VALUES(1)")
        connection.commit()

    if A9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'A9')"""):
            if row == (0,):
                print("A9 - miss")
                A9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("A9 - hit")
                A9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(A9) VALUES(1)")
        connection.commit()


    if B1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B1')"""):
            if row == (0,):
                print("B1 - miss")
                B1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B1 - hit")
                B1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B1) VALUES(1)")
        connection.commit()

    if B2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B2')"""):
            if row == (0,):
                print("B2 - miss")
                B2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B2 - hit")
                B2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B2) VALUES(1)")
        connection.commit()

    if B3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B3')"""):
            if row == (0,):
                print("B3 - miss")
                B3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B3 - hit")
                B3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B3) VALUES(1)")
        connection.commit()

    if B4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B4')"""):
            if row == (0,):
                print("B4 - miss")
                B4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B4 - hit")
                B4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B4) VALUES(1)")
        connection.commit()

    if B5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B5')"""):
            if row == (0,):
                print("B5 - miss")
                B5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B5 - hit")
                B5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B5) VALUES(1)")
        connection.commit()

    if B6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B6')"""):
            if row == (0,):
                print("B6 - miss")
                B6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B6 - hit")
                B6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B6) VALUES(1)")
        connection.commit()

    if B7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B7')"""):
            if row == (0,):
                print("B7 - miss")
                B7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B7 - hit")
                B7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B7) VALUES(1)")
        connection.commit()

    if B8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B8')"""):
            if row == (0,):
                print("B8 - miss")
                B8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B8 - hit")
                B8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B8) VALUES(1)")
        connection.commit()

    if B9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'B9')"""):
            if row == (0,):
                print("B9 - miss")
                B9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("B9 - hit")
                B9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(B9) VALUES(1)")
        connection.commit()


    if C1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C1')"""):
            if row == (0,):
                print("C1 - miss")
                C1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C1 - hit")
                C1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C1) VALUES(1)")
        connection.commit()

    if C2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C2')"""):
            if row == (0,):
                print("C2 - miss")
                C2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C2 - hit")
                C2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C2) VALUES(1)")
        connection.commit()

    if C3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C3')"""):
            if row == (0,):
                print("C3 - miss")
                C3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C3 - hit")
                C3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C3) VALUES(1)")
        connection.commit()

    if C4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C4')"""):
            if row == (0,):
                print("C4 - miss")
                C4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C4 - hit")
                C4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C4) VALUES(1)")
        connection.commit()

    if C5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C5')"""):
            if row == (0,):
                print("C5 - miss")
                C5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C5 - hit")
                C5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C5) VALUES(1)")
        connection.commit()

    if C6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C6')"""):
            if row == (0,):
                print("C6 - miss")
                C6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C6 - hit")
                C6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C6) VALUES(1)")
        connection.commit()

    if C7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C7')"""):
            if row == (0,):
                print("C7 - miss")
                C7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C7 - hit")
                C7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C7) VALUES(1)")
        connection.commit()

    if C8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C8')"""):
            if row == (0,):
                print("C8 - miss")
                C8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C8 - hit")
                C8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C8) VALUES(1)")
        connection.commit()

    if C9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'C9')"""):
            if row == (0,):
                print("C9 - miss")
                C9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("C9 - hit")
                C9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(C9) VALUES(1)")
        connection.commit()


    if D1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D1')"""):
            if row == (0,):
                print("D1 - miss")
                D1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D1 - hit")
                D1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D1) VALUES(1)")
        connection.commit()

    if D2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D2')"""):
            if row == (0,):
                print("D2 - miss")
                D2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D2 - hit")
                D2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D2) VALUES(1)")
        connection.commit()

    if D3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D3')"""):
            if row == (0,):
                print("D3 - miss")
                D3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D3 - hit")
                D3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D3) VALUES(1)")
        connection.commit()

    if D4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D4')"""):
            if row == (0,):
                print("D4 - miss")
                D4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D4 - hit")
                D4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D4) VALUES(1)")
        connection.commit()

    if D5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D5')"""):
            if row == (0,):
                print("D5 - miss")
                D5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D5 - hit")
                D5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D5) VALUES(1)")
        connection.commit()

    if D6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D6')"""):
            if row == (0,):
                print("D6 - miss")
                D6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D6 - hit")
                D6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D6) VALUES(1)")
        connection.commit()

    if D7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D7')"""):
            if row == (0,):
                print("D7 - miss")
                D7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D7 - hit")
                D7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D7) VALUES(1)")
        connection.commit()

    if D8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D8')"""):
            if row == (0,):
                print("D8 - miss")
                D8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D8 - hit")
                D8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D8) VALUES(1)")
        connection.commit()

    if D9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'D9')"""):
            if row == (0,):
                print("D9 - miss")
                D9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("D9 - hit")
                D9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(D9) VALUES(1)")
        connection.commit()


    if E1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E1')"""):
            if row == (0,):
                print("E1 - miss")
                E1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E1 - hit")
                E1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E1) VALUES(1)")
        connection.commit()

    if E2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E2')"""):
            if row == (0,):
                print("E2 - miss")
                E2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E2 - hit")
                E2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E2) VALUES(1)")
        connection.commit()

    if E3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E3')"""):
            if row == (0,):
                print("E3 - miss")
                E3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E3 - hit")
                E3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E3) VALUES(1)")
        connection.commit()

    if E4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E4')"""):
            if row == (0,):
                print("E4 - miss")
                E4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E4 - hit")
                E4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E4) VALUES(1)")
        connection.commit()

    if E5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E5')"""):
            if row == (0,):
                print("E5 - miss")
                E5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E5 - hit")
                E5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E5) VALUES(1)")
        connection.commit()

    if E6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E6')"""):
            if row == (0,):
                print("E6 - miss")
                E6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E6 - hit")
                E6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E6) VALUES(1)")
        connection.commit()

    if E7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E7')"""):
            if row == (0,):
                print("E7 - miss")
                E7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E7 - hit")
                E7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E7) VALUES(1)")
        connection.commit()

    if E8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E8')"""):
            if row == (0,):
                print("E8 - miss")
                E8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E8 - hit")
                E8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E8) VALUES(1)")
        connection.commit()

    if E9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'E9')"""):
            if row == (0,):
                print("E9 - miss")
                E9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("E9 - hit")
                E9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(E9) VALUES(1)")
        connection.commit()


    if F1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F1')"""):
            if row == (0,):
                print("F1 - miss")
                F1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F1 - hit")
                F1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F1) VALUES(1)")
        connection.commit()

    if F2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F2')"""):
            if row == (0,):
                print("F2 - miss")
                F2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F2 - hit")
                F2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F2) VALUES(1)")
        connection.commit()

    if F3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F3')"""):
            if row == (0,):
                print("F3 - miss")
                F3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F3 - hit")
                F3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F3) VALUES(1)")
        connection.commit()

    if F4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F4')"""):
            if row == (0,):
                print("F4 - miss")
                F4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F4 - hit")
                F4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F4) VALUES(1)")
        connection.commit()

    if F5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F5')"""):
            if row == (0,):
                print("F5 - miss")
                F5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F5 - hit")
                F5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F5) VALUES(1)")
        connection.commit()

    if F6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F6')"""):
            if row == (0,):
                print("F6 - miss")
                F6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F6 - hit")
                F6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F6) VALUES(1)")
        connection.commit()

    if F7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F7')"""):
            if row == (0,):
                print("F7 - miss")
                F7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F7 - hit")
                F7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F7) VALUES(1)")
        connection.commit()

    if F8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F8')"""):
            if row == (0,):
                print("F8 - miss")
                F8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F8 - hit")
                F8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F8) VALUES(1)")
        connection.commit()

    if F9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'F9')"""):
            if row == (0,):
                print("F9 - miss")
                F9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("F9 - hit")
                F9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(F9) VALUES(1)")
        connection.commit()


    if G1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G1')"""):
            if row == (0,):
                print("G1 - miss")
                G1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G1 - hit")
                G1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G1) VALUES(1)")
        connection.commit()

    if G2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G2')"""):
            if row == (0,):
                print("G2 - miss")
                G2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G2 - hit")
                G2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G2) VALUES(1)")
        connection.commit()

    if G3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G3')"""):
            if row == (0,):
                print("G3 - miss")
                G3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G3 - hit")
                G3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G3) VALUES(1)")
        connection.commit()

    if G4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G4')"""):
            if row == (0,):
                print("G4 - miss")
                G4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G4 - hit")
                G4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G4) VALUES(1)")
        connection.commit()

    if G5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G5')"""):
            if row == (0,):
                print("G5 - miss")
                G5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G5 - hit")
                G5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G5) VALUES(1)")
        connection.commit()

    if G6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G6')"""):
            if row == (0,):
                print("G6 - miss")
                G6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G6 - hit")
                G6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G6) VALUES(1)")
        connection.commit()

    if G7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G7')"""):
            if row == (0,):
                print("G7 - miss")
                G7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G7 - hit")
                G7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G7) VALUES(1)")
        connection.commit()

    if G8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G8')"""):
            if row == (0,):
                print("G8 - miss")
                G8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G8 - hit")
                G8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G8) VALUES(1)")
        connection.commit()

    if G9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'G9')"""):
            if row == (0,):
                print("G9 - miss")
                G9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("G9 - hit")
                G9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(G9) VALUES(1)")
        connection.commit()


    if H1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H1')"""):
            if row == (0,):
                print("H1 - miss")
                H1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H1 - hit")
                H1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H1) VALUES(1)")
        connection.commit()

    if H2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H2')"""):
            if row == (0,):
                print("H2 - miss")
                H2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H2 - hit")
                H2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H2) VALUES(1)")
        connection.commit()

    if H3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H3')"""):
            if row == (0,):
                print("H3 - miss")
                H3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H3 - hit")
                H3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H3) VALUES(1)")
        connection.commit()

    if H4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H4')"""):
            if row == (0,):
                print("H4 - miss")
                H4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H4 - hit")
                H4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H4) VALUES(1)")
        connection.commit()

    if H5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H5')"""):
            if row == (0,):
                print("H5 - miss")
                H5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H5 - hit")
                H5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H5) VALUES(1)")
        connection.commit()

    if H6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H6')"""):
            if row == (0,):
                print("H6 - miss")
                H6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H6 - hit")
                H6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H6) VALUES(1)")
        connection.commit()

    if H7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H7')"""):
            if row == (0,):
                print("H7 - miss")
                H7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H7 - hit")
                H7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H7) VALUES(1)")
        connection.commit()

    if H8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H8')"""):
            if row == (0,):
                print("H8 - miss")
                H8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H8 - hit")
                H8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H8) VALUES(1)")
        connection.commit()

    if H9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'H9')"""):
            if row == (0,):
                print("H9 - miss")
                H9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("H9 - hit")
                H9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(H9) VALUES(1)")
        connection.commit()


    if I1CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I1')"""):
            if row == (0,):
                print("I1 - miss")
                I1.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I1 - hit")
                I1.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I1) VALUES(1)")
        connection.commit()

    if I2CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I2')"""):
            if row == (0,):
                print("I2 - miss")
                I2.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I2 - hit")
                I2.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I2) VALUES(1)")
        connection.commit()

    if I3CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I3')"""):
            if row == (0,):
                print("I3 - miss")
                I3.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I3 - hit")
                I3.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I3) VALUES(1)")
        connection.commit()

    if I4CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I4')"""):
            if row == (0,):
                print("I4 - miss")
                I4.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I4 - hit")
                I4.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I4) VALUES(1)")
        connection.commit()

    if I5CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I5')"""):
            if row == (0,):
                print("I5 - miss")
                I5.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I5 - hit")
                I5.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I5) VALUES(1)")
        connection.commit()

    if I6CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I6')"""):
            if row == (0,):
                print("I6 - miss")
                I6.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I6 - hit")
                I6.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I6) VALUES(1)")
        connection.commit()

    if I7CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I7')"""):
            if row == (0,):
                print("I7 - miss")
                I7.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I7 - hit")
                I7.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I7) VALUES(1)")
        connection.commit()

    if I8CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I8')"""):
            if row == (0,):
                print("I8 - miss")
                I8.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I8 - hit")
                I8.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I8) VALUES(1)")
        connection.commit()

    if I9CLICKED is True:
        for row in cursor.execute("""SELECT EXISTS(select * from board_details
                                  WHERE player2_ships = 'I9')"""):
            if row == (0,):
                print("I9 - miss")
                I9.configure(fg="black", bg="white", state=DISABLED)

            if row == (1,):
                print("I9 - hit")
                I9.configure(fg="black", bg="red", state=DISABLED)

        cursor.execute("INSERT INTO p1_reveals(I9) VALUES(1)")
        connection.commit()


hitlabel = Button(root, text = (P1WIN_CON, " player 2 ship grids hit"),
                  bg="light green", activebackground="light yellow")
hitlabel.grid(row = 12, column = 0, columnspan = 2,)
print(P1WIN_CON , "/17 player 2 ship grids found")

root.mainloop()
