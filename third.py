from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlite3
from tkinter import messagebox


root = Tk()
root.title("PLAYER 1 SHIP PLACEMENTS")

#size, colour, and icon settings
root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open("images/battleship.jpg")))
root.geometry("900x600")
root.configure(background="light green")

#using frame to layout the buttons in a board, in the center
board1 = Frame(root, background="light green")
board1.place(relx=0.5, rely=0.5, anchor= CENTER,)

#connect to database and create a new table to run the game
connection = sqlite3.connect("battleships.db")
cursor = connection.cursor()

cursor.execute("""create table if not exists board_details
                (player1_ships text, player2_ships text, player1_guess text, player2_guess text)""")
connection.commit()

#to end the game without errors for the next time, the table is dropped
def gamequit():
    cursor.execute("DROP TABLE board_details")
    messagebox.showinfo("BATTLESHIPS", "killing game")
    root.quit()

#the quit button
button_exit=Button(board1, text="Exit Program",
                    bg="yellow", activebackground="red", activeforeground="white",
                    command = gamequit )
button_exit.grid(row=9, column=9)

#a function that checks if the ship count is less than 17 or runs next game state
def p1guessing():
    if P1_SHIPCOUNT < 17:
        messagebox.showinfo("!!!PLAYER 1!!!","CHOOSE ALL YOUR 17 SHIP SPACES BEFORE CONFIRMATION")

    else:
        messagebox.showinfo("PLAYER 1 CONFIRMED SHIPS", "NOW PLAYER 2 PICKS THEIR SHIP LOCATIONS")
        print("killing board1")
        root.destroy()
        subprocess.run(["python", ("fourth.py")])


#a function for the player to reset their decisions without restarting the entire program
#by setting all player one’s ship choices to null,
#then deleting from board_details where values are null, the board can be reloaded
def p1resetplace():
    cursor.execute("UPDATE board_details SET player1_ships = NULL")
    cursor.execute("""DELETE FROM board_details WHERE
                   player1_ships IS NULL AND player2_ships IS NULL""")
    connection.commit()
    messagebox.showinfo("PLAYER 1 BOARD", "SHIP SELECTION RESET")
    print("killing board1")
    root.destroy()
    subprocess.run(["python", ("third.py")])

#a button that uses p1guessing to confirm the players ship choices and move to the next game state
p1_con_place = Button(root, text="CONFIRM SHIP PLACEMENT", padx = 10, pady = 5,
                      fg="orange", bg="black", activebackground="orange", activeforeground="black",
                      command = p1guessing)
p1_con_place.grid()

#a button in the top left that uses p1resetplace command defined earlier
p1_res_place = Button(root, text="reset placement", padx = 10, pady = 5,
                      fg="orange", bg="black", activebackground="orange", activeforeground="black",
                      command = p1resetplace)
p1_res_place.grid()


#Define global ship count at 0, and is incremented each time a board button is pressed
P1_SHIPCOUNT = 0

playerlabel = Label(text="PLAYER 1:", bg="light green")
playerlabel.grid(row=7, column=0)

#count display
countlabel = Button(root, text = "place ships of any size",
                    bg="light green", activebackground="light yellow")
countlabel.grid(row = 9, column = 0, columnspan = 2,)

limitlabel = Label(text="(no more or less than 17 spaces)", bg="light green")
limitlabel.grid(row=10, column=0)

#Before first click, set to false, variable for all buttons
# to record when they have been CLICKED is set to true
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

#checks each XYCLICKED if they are true or false,
    #changing their colour to white and state to disabled if they haven’t been CLICKED.
    #   (disabling all buttons that haven’t been already CLICKED and colouring them white)
def shiplimit():
 
    if A1CLICKED == False:
        A1.configure(fg="black", bg="white", state=DISABLED)
    if A2CLICKED == False:
        A2.configure(fg="black", bg="white", state=DISABLED)
    if A3CLICKED == False:
        A3.configure(fg="black", bg="white", state=DISABLED)
    if A4CLICKED == False:
        A4.configure(fg="black", bg="white", state=DISABLED)
    if A5CLICKED == False:
        A5.configure(fg="black", bg="white", state=DISABLED)
    if A6CLICKED == False:
        A6.configure(fg="black", bg="white", state=DISABLED)
    if A7CLICKED == False:
        A7.configure(fg="black", bg="white", state=DISABLED)
    if A8CLICKED == False:
        A8.configure(fg="black", bg="white", state=DISABLED)
    if A9CLICKED == False:
        A9.configure(fg="black", bg="white", state=DISABLED)
    
    
    if B1CLICKED == False:
        B1.configure(fg="black", bg="white", state=DISABLED)
    if B2CLICKED == False:
        B2.configure(fg="black", bg="white", state=DISABLED)
    if B3CLICKED == False:
        B3.configure(fg="black", bg="white", state=DISABLED)
    if B4CLICKED == False:
        B4.configure(fg="black", bg="white", state=DISABLED)
    if B5CLICKED == False:
        B5.configure(fg="black", bg="white", state=DISABLED)
    if B6CLICKED == False:
        B6.configure(fg="black", bg="white", state=DISABLED)
    if B7CLICKED == False:
        B7.configure(fg="black", bg="white", state=DISABLED)
    if B8CLICKED == False:
        B8.configure(fg="black", bg="white", state=DISABLED)
    if B9CLICKED == False:
        B9.configure(fg="black", bg="white", state=DISABLED)

    if C1CLICKED == False:
        C1.configure(fg="black", bg="white", state=DISABLED)
    if C2CLICKED == False:
        C2.configure(fg="black", bg="white", state=DISABLED)
    if C3CLICKED == False:
        C3.configure(fg="black", bg="white", state=DISABLED)
    if C4CLICKED == False:
        C4.configure(fg="black", bg="white", state=DISABLED)
    if C5CLICKED == False:
        C5.configure(fg="black", bg="white", state=DISABLED)
    if C6CLICKED == False:
        C6.configure(fg="black", bg="white", state=DISABLED)
    if C7CLICKED == False:
        C7.configure(fg="black", bg="white", state=DISABLED)
    if C8CLICKED == False:
        C8.configure(fg="black", bg="white", state=DISABLED)
    if C9CLICKED == False:
        C9.configure(fg="black", bg="white", state=DISABLED)
        
    if D1CLICKED == False:
        D1.configure(fg="black", bg="white", state=DISABLED)
    if D2CLICKED == False:
        D2.configure(fg="black", bg="white", state=DISABLED)
    if D3CLICKED == False:
        D3.configure(fg="black", bg="white", state=DISABLED)
    if D4CLICKED == False:
        D4.configure(fg="black", bg="white", state=DISABLED)
    if D5CLICKED == False:
        D5.configure(fg="black", bg="white", state=DISABLED)
    if D6CLICKED == False:
        D6.configure(fg="black", bg="white", state=DISABLED)
    if D7CLICKED == False:
        D7.configure(fg="black", bg="white", state=DISABLED)
    if D8CLICKED == False:
        D8.configure(fg="black", bg="white", state=DISABLED)
    if D9CLICKED == False:
        D9.configure(fg="black", bg="white", state=DISABLED)
        
    if E1CLICKED == False:
        E1.configure(fg="black", bg="white", state=DISABLED)
    if E2CLICKED == False:
        E2.configure(fg="black", bg="white", state=DISABLED)
    if E3CLICKED == False:
        E3.configure(fg="black", bg="white", state=DISABLED)
    if E4CLICKED == False:
        E4.configure(fg="black", bg="white", state=DISABLED)
    if E5CLICKED == False:
        E5.configure(fg="black", bg="white", state=DISABLED)
    if E6CLICKED == False:
        E6.configure(fg="black", bg="white", state=DISABLED)
    if E7CLICKED == False:
        E7.configure(fg="black", bg="white", state=DISABLED)
    if E8CLICKED == False:
        E8.configure(fg="black", bg="white", state=DISABLED)
    if E9CLICKED == False:
        E9.configure(fg="black", bg="white", state=DISABLED)
        
    if F1CLICKED == False:
        F1.configure(fg="black", bg="white", state=DISABLED)
    if F2CLICKED == False:
        F2.configure(fg="black", bg="white", state=DISABLED)
    if F3CLICKED == False:
        F3.configure(fg="black", bg="white", state=DISABLED)
    if F4CLICKED == False:
        F4.configure(fg="black", bg="white", state=DISABLED)
    if F5CLICKED == False:
        F5.configure(fg="black", bg="white", state=DISABLED)
    if F6CLICKED == False:
        F6.configure(fg="black", bg="white", state=DISABLED)
    if F7CLICKED == False:
        F7.configure(fg="black", bg="white", state=DISABLED)
    if F8CLICKED == False:
        F8.configure(fg="black", bg="white", state=DISABLED)
    if F9CLICKED == False:
        F9.configure(fg="black", bg="white", state=DISABLED)
        
    if G1CLICKED == False:
        G1.configure(fg="black", bg="white", state=DISABLED)
    if G2CLICKED == False:
        G2.configure(fg="black", bg="white", state=DISABLED)
    if G3CLICKED == False:
        G3.configure(fg="black", bg="white", state=DISABLED)
    if G4CLICKED == False:
        G4.configure(fg="black", bg="white", state=DISABLED)
    if G5CLICKED == False:
        G5.configure(fg="black", bg="white", state=DISABLED)
    if G6CLICKED == False:
        G6.configure(fg="black", bg="white", state=DISABLED)
    if G7CLICKED == False:
        G7.configure(fg="black", bg="white", state=DISABLED)
    if G8CLICKED == False:
        G8.configure(fg="black", bg="white", state=DISABLED)
    if G9CLICKED == False:
        G9.configure(fg="black", bg="white", state=DISABLED)
    
    if H1CLICKED == False:
        H1.configure(fg="black", bg="white", state=DISABLED)
    if H2CLICKED == False:
        H2.configure(fg="black", bg="white", state=DISABLED)
    if H3CLICKED == False:
        H3.configure(fg="black", bg="white", state=DISABLED)
    if H4CLICKED == False:
        H4.configure(fg="black", bg="white", state=DISABLED)
    if H5CLICKED == False:
        H5.configure(fg="black", bg="white", state=DISABLED)
    if H6CLICKED == False:
        H6.configure(fg="black", bg="white", state=DISABLED)
    if H7CLICKED == False:
        H7.configure(fg="black", bg="white", state=DISABLED)
    if H8CLICKED == False:
        H8.configure(fg="black", bg="white", state=DISABLED)
    if H9CLICKED == False:
        H9.configure(fg="black", bg="white", state=DISABLED)
        
    if I1CLICKED == False:
        I1.configure(fg="black", bg="white", state=DISABLED)
    if I2CLICKED == False:
        I2.configure(fg="black", bg="white", state=DISABLED)
    if I3CLICKED == False:
        I3.configure(fg="black", bg="white", state=DISABLED)
    if I4CLICKED == False:
        I4.configure(fg="black", bg="white", state=DISABLED)
    if I5CLICKED == False:
        I5.configure(fg="black", bg="white", state=DISABLED)
    if I6CLICKED == False:
        I6.configure(fg="black", bg="white", state=DISABLED)
    if I7CLICKED == False:
        I7.configure(fg="black", bg="white", state=DISABLED)
    if I8CLICKED == False:
        I8.configure(fg="black", bg="white", state=DISABLED)
    if I9CLICKED == False:
        I9.configure(fg="black", bg="white", state=DISABLED)



#for each unique board button:
def xAy1():
    global A1CLICKED
    A1CLICKED = not A1CLICKED # Changes XYCLICKED to true

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Increments the global ship count + 1
    # Displays / Prints number of ships placed
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")

    # Sets the corresponding button to green and disabled, (feedback to user that its selected)
    A1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17: # Checks if ship count is greater than or equal to 17
       shiplimit() #disables the board to prevent more than 17 grids being chosen

    # Inserts relevant coordinates into board details (player1_ships)
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A1')")
    # Prints the database into the terminal
    for row in cursor.execute("select * from board_details "): print(row)

    connection.commit()




def xAy2():
    global A2CLICKED
    A2CLICKED = not A2CLICKED

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A2.configure(fg="black", bg="green", state=DISABLED)
    
    if P1_SHIPCOUNT >= 17:
       shiplimit()

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A2')")
    
    for row in cursor.execute("select * from board_details "): print(row)

    connection.commit()



def xAy3():
    global A3CLICKED
    A3CLICKED = not A3CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xAy4():
    global A4CLICKED
    A4CLICKED = not A4CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xAy5():
    global A5CLICKED
    A5CLICKED = not A5CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xAy6():
    global A6CLICKED
    A6CLICKED = not A6CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xAy7():
    global A7CLICKED
    A7CLICKED = not A7CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xAy8():
    global A8CLICKED
    A8CLICKED = not A8CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xAy9():
    global A9CLICKED
    A9CLICKED = not A9CLICKED

    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('A9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    A9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()


 
def xBy1():
    global B1CLICKED
    B1CLICKED = not B1CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy2():
    global B2CLICKED
    B2CLICKED = not B2CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy3():
    global B3CLICKED
    B3CLICKED = not B3CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy4():
    global B4CLICKED
    B4CLICKED = not B4CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy5():
    global B5CLICKED
    B5CLICKED = not B5CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B5.configure(fg="black", bg="green", state=DISABLED)
    
    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy6():
    global B6CLICKED
    B6CLICKED = not B6CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B6.configure(fg="black", bg="green", state=DISABLED)
    
    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy7():
    global B7CLICKED
    B7CLICKED = not B7CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B7.configure(fg="black", bg="green", state=DISABLED)
    
    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy8():
    global B8CLICKED
    B8CLICKED = not B8CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B8.configure(fg="black", bg="green", state=DISABLED)
    
    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xBy9():
    global B9CLICKED
    B9CLICKED = not B9CLICKED 
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('B9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    B9.configure(fg="black", bg="green", state=DISABLED)
    
    if P1_SHIPCOUNT >= 17:
       shiplimit()

 

    
def xCy1():
    global C1CLICKED
    C1CLICKED = not C1CLICKED
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy2():
    global C2CLICKED
    C2CLICKED = not C2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy3():
    global C3CLICKED
    C3CLICKED = not C3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy4():
    global C4CLICKED
    C4CLICKED = not C4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy5():
    global C5CLICKED
    C5CLICKED = not C5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy6():
    global C6CLICKED
    C6CLICKED = not C6CLICKED  
     
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy7():
    global C7CLICKED
    C7CLICKED = not C7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy8():
    global C8CLICKED
    C8CLICKED = not C8CLICKED
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xCy9():
    global C9CLICKED
    C9CLICKED = not C9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('C9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    C9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()



 
def xDy1():
    global D1CLICKED
    D1CLICKED = not D1CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy2():
    global D2CLICKED
    D2CLICKED = not D2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy3():
    global D3CLICKED
    D3CLICKED = not D3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy4():
    global D4CLICKED
    D4CLICKED = not D4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy5():
    global D5CLICKED
    D5CLICKED = not D5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy6():
    global D6CLICKED
    D6CLICKED = not D6CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy7():
    global D7CLICKED
    D7CLICKED = not D7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy8():
    global D8CLICKED
    D8CLICKED = not D8CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xDy9():
    global D9CLICKED
    D9CLICKED = not D9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('D9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    D9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()



def xEy1():
    global E1CLICKED
    E1CLICKED = not E1CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy2():
    global E2CLICKED
    E2CLICKED = not E2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy3():
    global E3CLICKED
    E3CLICKED = not E3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy4():
    global E4CLICKED
    E4CLICKED = not E4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy5():
    global E5CLICKED
    E5CLICKED = not E5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy6():
    global E6CLICKED
    E6CLICKED = not E6CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy7():
    global E7CLICKED
    E7CLICKED = not E7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy8():
    global E8CLICKED
    E8CLICKED = not E8CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xEy9():
    global E9CLICKED
    E9CLICKED = not E9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('E9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    E9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()




def xFy1():
    global F1CLICKED
    F1CLICKED = not F1CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy2():
    global F2CLICKED
    F2CLICKED = not F2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy3():
    global F3CLICKED
    F3CLICKED = not F3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy4():
    global F4CLICKED
    F4CLICKED = not F4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy5():
    global F5CLICKED
    F5CLICKED = not F5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy6():
    global F6CLICKED
    F6CLICKED = not F6CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy7():
    global F7CLICKED
    F7CLICKED = not F7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy8():
    global F8CLICKED
    F8CLICKED = not F8CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xFy9():
    global F9CLICKED
    F9CLICKED = not F9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('F9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    F9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()




def xGy1():
    global G1CLICKED
    G1CLICKED = not G1CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy2():
    global G2CLICKED
    G2CLICKED = not G2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy3():
    global G3CLICKED
    G3CLICKED = not G3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy4():
    global G4CLICKED
    G4CLICKED = not G4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy5():
    global G5CLICKED
    G5CLICKED = not G5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy6():
    global G6CLICKED
    G6CLICKED = not G6CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy7():
    global G7CLICKED
    G7CLICKED = not G7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy8():
    global G8CLICKED
    G8CLICKED = not G8CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xGy9():
    global G9CLICKED
    G9CLICKED = not G9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('G9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    G9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()




def xHy1():
    global H1CLICKED
    H1CLICKED = not H1CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy2():
    global H2CLICKED
    H2CLICKED = not H2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy3():
    global H3CLICKED
    H3CLICKED = not H3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy4():
    global H4CLICKED
    H4CLICKED = not H4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy5():
    global H5CLICKED
    H5CLICKED = not H5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy6():
    global H6CLICKED
    H6CLICKED = not H6CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy7():
    global H7CLICKED
    H7CLICKED = not H7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy8():
    global H8CLICKED
    H8CLICKED = not H8CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xHy9():
    global H9CLICKED
    H9CLICKED = not H9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('H9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    H9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()




def xIy1():
    global I1CLICKED
    I1CLICKED = not I1CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I1')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I1.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy2():
    global I2CLICKED
    I2CLICKED = not I2CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I2')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I2.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy3():
    global I3CLICKED
    I3CLICKED = not I3CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I3')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I3.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy4():
    global I4CLICKED
    I4CLICKED = not I4CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I4')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I4.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy5():
    global I5CLICKED
    I5CLICKED = not I5CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I5')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I5.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy6():
    global I6CLICKED
    I6CLICKED = not I6CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I6')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I6.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy7():
    global I7CLICKED
    I7CLICKED = not I7CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I7')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I7.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy8():
    global I8CLICKED
    I8CLICKED = not I8CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I8')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I8.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()

def xIy9():
    global I9CLICKED
    I9CLICKED = not I9CLICKED  
    
    cursor.execute("INSERT INTO board_details(player1_ships) VALUES('I9')")
    
    for row in cursor.execute("select * from board_details "): print(row)
    connection.commit()

    global P1_SHIPCOUNT
    P1_SHIPCOUNT += 1  # Update value of global variable.
    countlabel.config(text= (P1_SHIPCOUNT, " ship grids chosen"))
    print(P1_SHIPCOUNT , " ship grids placed")


    I9.configure(fg="black", bg="green", state=DISABLED)

    if P1_SHIPCOUNT >= 17:
       shiplimit()


#each of the buttons layout on the board, with their unique commands
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
