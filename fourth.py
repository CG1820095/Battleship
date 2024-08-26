"""tkinter provides the majority of functions for the gui"""
from tkinter import Tk, Frame, CENTER, Button, Label, DISABLED, messagebox
import subprocess
import sqlite3
from PIL import ImageTk, Image


root = Tk()
root.title("PLAYER 2 SHIP PLACEMENTS")

root.tk.call('wm', 'iconphoto', root, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.geometry("900x600")
root.configure(background="pink")


connection = sqlite3.connect("battleships.db")
cursor =connection.cursor()


cursor.execute("""create table if not exists board_details
                (player1_ships text, player2_ships text, player1_guess text, player2_guess text)""")
connection.commit()

board2 = Frame(root, background="pink")
board2.place(relx=0.5, rely=0.5, anchor= CENTER)


def gamequit():
    """Function drops table and quits game"""
    cursor.execute("DROP TABLE board_details")
    messagebox.showinfo("BATTLESHIPS", "killing game")
    root.quit()

button_exit=Button(board2, text="Exit Program",
                    bg="yellow", activebackground="red", activeforeground="white",
                    command = gamequit)
button_exit.grid(row=9, column=9)


def p2guessing():
    """Function checks if player 2's ship count is valid to progress to player 1's guess"""
    if P2_SHIPCOUNT < 17:
        messagebox.showinfo("!!!","CHOOSE ALL YOUR 17 SHIP SPACES BEFORE CONFIRMATION")
    else:
        messagebox.showinfo("PLAYER 2 CONFIRMED SHIP POSITIONS",
                            "NOW PLAYER 1 GUESSES PLAYER 2'S SHIP LOCATIONS")
        print("killing board2")
        root.destroy()
        subprocess.run(["python", ("fifth.py")], check=False)

def p2resetplace():
    """Function allows player to change their ship choices"""
    cursor.execute("UPDATE board_details SET player2_ships = NULL")
    cursor.execute("""DELETE FROM board_details WHERE
                   player1_ships IS NULL AND player2_ships IS NULL""")
    connection.commit()
    messagebox.showinfo("PLAYER 2 BOARD", "SHIP SELECTION RESET")
    print("killing board2")
    root.destroy()
    subprocess.run(["python", ("fourth.py")], check=False)


p2_con_place = Button(root, text="CONFIRM SHIP PLACEMENT", padx = 10, pady = 5,
                      fg="orange", bg="black", activebackground="orange", activeforeground="black",
                      command = p2guessing)
p2_con_place.grid()

p2_res_place = Button(root, text="reset placement", padx = 10, pady = 5,
                      fg="orange", bg="black", activebackground="orange", activeforeground="black",
                      command = p2resetplace)
p2_res_place.grid()


#Define global ship count.
P2_SHIPCOUNT = 0

playerlabel = Label(text="PLAYER 2:", bg="light pink",)
playerlabel.grid(row=7, column=0)

#count display
countlabel = Button(root, text = "place ships of any size",
                    bg="light pink", activebackground="light yellow")
countlabel.grid(row = 9, column = 0, columnspan = 2,)

maxlabel = Label(text="(no more or less than 17 spaces)", bg="light pink",)
maxlabel.grid(row=10, column=0)


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


def shiplimit():
    """Function locks board buttons that haven't been clicked, when ship limit is hit""" 
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


#for each unique board button:
def xay1():
    """Function for the grid coordinate"""
    global A1CLICKED
    A1CLICKED = not A1CLICKED # Changes XYCLICKED to true

    # Inserts relevant coordinates into board details (player2_ships)
    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A1')")
    # Prints the database into the terminal
    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Increments the global ship count + 1
    # Displays / Prints number of ships placed
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")

    # Sets the corresponding button to green and disabled, (feedback to user that its selected)
    A1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17: # Checks if ship count is greater than or equal to 17
        shiplimit() #disables the board to prevent more than 17 grids being chosen


def xay2():
    """Function for the grid coordinate"""
    global A2CLICKED
    A2CLICKED = not A2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay3():
    """Function for the grid coordinate"""
    global A3CLICKED
    A3CLICKED = not A3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay4():
    """Function for the grid coordinate"""
    global A4CLICKED
    A4CLICKED = not A4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay5():
    """Function for the grid coordinate"""
    global A5CLICKED
    A5CLICKED = not A5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay6():
    """Function for the grid coordinate"""
    global A6CLICKED
    A6CLICKED = not A6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay7():
    """Function for the grid coordinate"""
    global A7CLICKED
    A7CLICKED = not A7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay8():
    """Function for the grid coordinate"""
    global A8CLICKED
    A8CLICKED = not A8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xay9():
    """Function for the grid coordinate"""
    global A9CLICKED
    A9CLICKED = not A9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('A9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    A9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()



def xby1():
    """Function for the grid coordinate"""
    global B1CLICKED
    B1CLICKED = not B1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby2():
    """Function for the grid coordinate"""
    global B2CLICKED
    B2CLICKED = not B2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby3():
    """Function for the grid coordinate"""
    global B3CLICKED
    B3CLICKED = not B3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby4():
    """Function for the grid coordinate"""
    global B4CLICKED
    B4CLICKED = not B4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby5():
    """Function for the grid coordinate"""
    global B5CLICKED
    B5CLICKED = not B5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby6():
    """Function for the grid coordinate"""
    global B6CLICKED
    B6CLICKED = not B6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby7():
    """Function for the grid coordinate"""
    global B7CLICKED
    B7CLICKED = not B7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby8():
    """Function for the grid coordinate"""
    global B8CLICKED
    B8CLICKED = not B8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xby9():
    """Function for the grid coordinate"""
    global B9CLICKED
    B9CLICKED = not B9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('B9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    B9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()



def xcy1():
    """Function for the grid coordinate"""
    global C1CLICKED
    C1CLICKED = not C1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy2():
    """Function for the grid coordinate"""
    global C2CLICKED
    C2CLICKED = not C2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy3():
    """Function for the grid coordinate"""
    global C3CLICKED
    C3CLICKED = not C3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy4():
    """Function for the grid coordinate"""
    global C4CLICKED
    C4CLICKED = not C4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy5():
    """Function for the grid coordinate"""
    global C5CLICKED
    C5CLICKED = not C5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy6():
    """Function for the grid coordinate"""
    global C6CLICKED
    C6CLICKED = not C6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy7():
    """Function for the grid coordinate"""
    global C7CLICKED
    C7CLICKED = not C7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy8():
    """Function for the grid coordinate"""
    global C8CLICKED
    C8CLICKED = not C8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xcy9():
    """Function for the grid coordinate"""
    global C9CLICKED
    C9CLICKED = not C9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('C9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    C9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()



def xdy1():
    """Function for the grid coordinate"""
    global D1CLICKED
    D1CLICKED = not D1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy2():
    """Function for the grid coordinate"""
    global D2CLICKED
    D2CLICKED = not D2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy3():
    """Function for the grid coordinate"""
    global D3CLICKED
    D3CLICKED = not D3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy4():
    """Function for the grid coordinate"""
    global D4CLICKED
    D4CLICKED = not D4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy5():
    """Function for the grid coordinate"""
    global D5CLICKED
    D5CLICKED = not D5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy6():
    """Function for the grid coordinate"""
    global D6CLICKED
    D6CLICKED = not D6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy7():
    """Function for the grid coordinate"""
    global D7CLICKED
    D7CLICKED = not D7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy8():
    """Function for the grid coordinate"""
    global D8CLICKED
    D8CLICKED = not D8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xdy9():
    """Function for the grid coordinate"""
    global D9CLICKED
    D9CLICKED = not D9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('D9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    D9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()



def xey1():
    """Function for the grid coordinate"""
    global E1CLICKED
    E1CLICKED = not E1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey2():
    """Function for the grid coordinate"""
    global E2CLICKED
    E2CLICKED = not E2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey3():
    """Function for the grid coordinate"""
    global E3CLICKED
    E3CLICKED = not E3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey4():
    """Function for the grid coordinate"""
    global E4CLICKED
    E4CLICKED = not E4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey5():
    """Function for the grid coordinate"""
    global E5CLICKED
    E5CLICKED = not E5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey6():
    """Function for the grid coordinate"""
    global E6CLICKED
    E6CLICKED = not E6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey7():
    """Function for the grid coordinate"""
    global E7CLICKED
    E7CLICKED = not E7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey8():
    """Function for the grid coordinate"""
    global E8CLICKED
    E8CLICKED = not E8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xey9():
    """Function for the grid coordinate"""
    global E9CLICKED
    E9CLICKED = not E9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('E9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    E9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()




def xfy1():
    """Function for the grid coordinate"""
    global F1CLICKED
    F1CLICKED = not F1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy2():
    """Function for the grid coordinate"""
    global F2CLICKED
    F2CLICKED = not F2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy3():
    """Function for the grid coordinate"""
    global F3CLICKED
    F3CLICKED = not F3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy4():
    """Function for the grid coordinate"""
    global F4CLICKED
    F4CLICKED = not F4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy5():
    """Function for the grid coordinate"""
    global F5CLICKED
    F5CLICKED = not F5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy6():
    """Function for the grid coordinate"""
    global F6CLICKED
    F6CLICKED = not F6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy7():
    """Function for the grid coordinate"""
    global F7CLICKED
    F7CLICKED = not F7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy8():
    """Function for the grid coordinate"""
    global F8CLICKED
    F8CLICKED = not F8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xfy9():
    """Function for the grid coordinate"""
    global F9CLICKED
    F9CLICKED = not F9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('F9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    F9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()




def xgy1():
    """Function for the grid coordinate"""
    global G1CLICKED
    G1CLICKED = not G1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy2():
    """Function for the grid coordinate"""
    global G2CLICKED
    G2CLICKED = not G2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy3():
    """Function for the grid coordinate"""
    global G3CLICKED
    G3CLICKED = not G3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy4():
    """Function for the grid coordinate"""
    global G4CLICKED
    G4CLICKED = not G4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy5():
    """Function for the grid coordinate"""
    global G5CLICKED
    G5CLICKED = not G5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy6():
    """Function for the grid coordinate"""
    global G6CLICKED
    G6CLICKED = not G6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy7():
    """Function for the grid coordinate"""
    global G7CLICKED
    G7CLICKED = not G7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy8():
    """Function for the grid coordinate"""
    global G8CLICKED
    G8CLICKED = not G8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xgy9():
    """Function for the grid coordinate"""
    global G9CLICKED
    G9CLICKED = not G9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('G9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    G9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()




def xhy1():
    """Function for the grid coordinate"""
    global H1CLICKED
    H1CLICKED = not H1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy2():
    """Function for the grid coordinate"""
    global H2CLICKED
    H2CLICKED = not H2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy3():
    """Function for the grid coordinate"""
    global H3CLICKED
    H3CLICKED = not H3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy4():
    """Function for the grid coordinate"""
    global H4CLICKED
    H4CLICKED = not H4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy5():
    """Function for the grid coordinate"""
    global H5CLICKED
    H5CLICKED = not H5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy6():
    """Function for the grid coordinate"""
    global H6CLICKED
    H6CLICKED = not H6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy7():
    """Function for the grid coordinate"""
    global H7CLICKED
    H7CLICKED = not H7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy8():
    """Function for the grid coordinate"""
    global H8CLICKED
    H8CLICKED = not H8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xhy9():
    """Function for the grid coordinate"""
    global H9CLICKED
    H9CLICKED = not H9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('H9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    H9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()




def xiy1():
    """Function for the grid coordinate"""
    global I1CLICKED
    I1CLICKED = not I1CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I1')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I1.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy2():
    """Function for the grid coordinate"""
    global I2CLICKED
    I2CLICKED = not I2CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I2')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I2.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy3():
    """Function for the grid coordinate"""
    global I3CLICKED
    I3CLICKED = not I3CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I3')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I3.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy4():
    """Function for the grid coordinate"""
    global I4CLICKED
    I4CLICKED = not I4CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I4')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I4.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy5():
    """Function for the grid coordinate"""
    global I5CLICKED
    I5CLICKED = not I5CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I5')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I5.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy6():
    """Function for the grid coordinate"""
    global I6CLICKED
    I6CLICKED = not I6CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I6')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I6.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy7():
    """Function for the grid coordinate"""
    global I7CLICKED
    I7CLICKED = not I7CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I7')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I7.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy8():
    """Function for the grid coordinate"""
    global I8CLICKED
    I8CLICKED = not I8CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I8')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I8.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()

def xiy9():
    """Function for the grid coordinate"""
    global I9CLICKED
    I9CLICKED = not I9CLICKED

    cursor.execute("INSERT INTO board_details(player2_ships) VALUES('I9')")

    for row in cursor.execute("select * from board_details "):
        print(row)
    connection.commit()

    global P2_SHIPCOUNT
    P2_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P2_SHIPCOUNT, " ship grids chosen"))
    print(P2_SHIPCOUNT , " ship grids placed")


    I9.configure(fg="black", bg="green", state=DISABLED)

    if P2_SHIPCOUNT >= 17:
        shiplimit()


#defininf each of the buttons layout on the board, with their unique commands
A1 = Button(board2, text="A1", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xay1,)
A2 = Button(board2, text="A2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay2)
A3 = Button(board2, text="A3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay3)
A4 = Button(board2, text="A4", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xay4)
A5 = Button(board2, text="A5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay5)
A6 = Button(board2, text="A6", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xay6)
A7 = Button(board2, text="A7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay7)
A8 = Button(board2, text="A8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xay8)
A9 = Button(board2, text="A9", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xay9)


B1 = Button(board2, text="B1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby1)
B2 = Button(board2, text="B2", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby2)
B3 = Button(board2, text="B3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby3)
B4 = Button(board2, text="B4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby4)
B5 = Button(board2, text="B5", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby5)
B6 = Button(board2, text="B6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby6)
B7 = Button(board2, text="B7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby7)
B8 = Button(board2, text="B8", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xby8)
B9 = Button(board2, text="B9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xby9)


C1 = Button(board2, text="C1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy1)
C2 = Button(board2, text="C2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy2)
C3 = Button(board2, text="C3", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xcy3)
C4 = Button(board2, text="C4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy4)
C5 = Button(board2, text="C5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy5)
C6 = Button(board2, text="C6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy6)
C7 = Button(board2, text="C7", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xcy7)
C8 = Button(board2, text="C8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy8)
C9 = Button(board2, text="C9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xcy9)


D1 = Button(board2, text="D1", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xdy1)
D2 = Button(board2, text="D2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy2)
D3 = Button(board2, text="D3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy3)
D4 = Button(board2, text="D4", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xdy4)
D5 = Button(board2, text="D5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy5)
D6 = Button(board2, text="D6", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xdy6)
D7 = Button(board2, text="D7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy7)
D8 = Button(board2, text="D8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xdy8)
D9 = Button(board2, text="D9", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xdy9)


E1 = Button(board2, text="E1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey1)
E2 = Button(board2, text="E2", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey2)
E3 = Button(board2, text="E3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey3)
E4 = Button(board2, text="E4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey4)
E5 = Button(board2, text="E5", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey5)
E6 = Button(board2, text="E6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey6)
E7 = Button(board2, text="E7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey7)
E8 = Button(board2, text="E8", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xey8)
E9 = Button(board2, text="E9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xey9)


F1 = Button(board2, text="F1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy1)
F2 = Button(board2, text="F2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy2)
F3 = Button(board2, text="F3", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xfy3)
F4 = Button(board2, text="F4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy4)
F5 = Button(board2, text="F5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy5)
F6 = Button(board2, text="F6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy6)
F7 = Button(board2, text="F7", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xfy7)
F8 = Button(board2, text="F8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy8)
F9 = Button(board2, text="F9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xfy9)


G1 = Button(board2, text="G1", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xgy1)
G2 = Button(board2, text="G2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy2)
G3 = Button(board2, text="G3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy3)
G4 = Button(board2, text="G4", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xgy4)
G5 = Button(board2, text="G5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy5)
G6 = Button(board2, text="G6", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xgy6)
G7 = Button(board2, text="G7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy7)
G8 = Button(board2, text="G8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xgy8)
G9 = Button(board2, text="G9", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xgy9)


H1 = Button(board2, text="H1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy1)
H2 = Button(board2, text="H2", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy2)
H3 = Button(board2, text="H3", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy3)
H4 = Button(board2, text="H4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy4)
H5 = Button(board2, text="H5", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy5)
H6 = Button(board2, text="H6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy6)
H7 = Button(board2, text="H7", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy7)
H8 = Button(board2, text="H8", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xhy8)
H9 = Button(board2, text="H9", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xhy9)


I1 = Button(board2, text="I1", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy1)
I2 = Button(board2, text="I2", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy2)
I3 = Button(board2, text="I3", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xiy3)
I4 = Button(board2, text="I4", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy4)
I5 = Button(board2, text="I5", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy5)
I6 = Button(board2, text="I6", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy6)
I7 = Button(board2, text="I7", padx = 15, pady = 15,
            fg="white", bg="blue", activebackground="hot pink", command = xiy7)
I8 = Button(board2, text="I8", padx = 15, pady = 15,
            fg="black", bg="light blue", activebackground="hot pink", command = xiy8)
I9 = Button(board2, text="I9", padx = 15, pady = 15,
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


root.mainloop()
