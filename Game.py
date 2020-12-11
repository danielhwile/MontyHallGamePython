from tkinter import *
import random
player_choice = None

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
# This initial Window is for the player to select the door, there will be two more frames, one for the reveal
# and a final frame to announce the results of the game
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        self.master.title("Monty Hall Door Game")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        L1 = Label(self, text="Please Select a Door!")
        L1.place(x=30,y=30)

        # creating a button instance
        door1_button = Button(self, text="Door One", command= self.client_exit1)
        door2_button = Button(self, text="Door Two", command= self.client_exit2)
        door3_button = Button(self, text="Door Three", command= self.client_exit3)
        # placing the button on my window
        door1_button.place(x=60, y=80)
        door2_button.place(x=60, y=110)
        door3_button.place(x=55, y=140)
    def client_exit1(self):
        global player_choice
        player_choice = 1
        root.destroy()
        return player_choice

    def client_exit2(self):
        global player_choice
        player_choice = 2
        root.destroy()
        return player_choice

    def client_exit3(self):
        global player_choice
        player_choice = 3
        root.destroy()
        return player_choice


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("200x200")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
change = None
winning_door = random.randint(1,3)
def door_revealer(choice,win):
    x = 0
    while x == 0:
        n = random.randint(1,3)
        if n != choice and n != win:
            x = 1
            return n
reveal = door_revealer(player_choice,winning_door)
#This is now our second Window, Extremely similar to the first, just different Text Show to the user, and different buttons
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("Monty Hall Door Game")

        self.pack(fill=BOTH, expand=1)

        L1 = Label(self, text="I will Now Show you a Losing Door!")
        L1.place(x=5,y=30)
        L2 = Label(self, text="Door #......")
        L2.place(x=60, y=50)
        L3 = Label(self, text=reveal)
        L3.place(x=90, y=65)
        L4 = Label(self, text="Would You like to Change Doors?")
        L4.place(x=5, y=90)

        switch_door_yes = Button(self, text="Yes", command= self.client_exit_yes)
        switch_door_no = Button(self, text="No", command= self.client_exit_no)

        switch_door_yes.place(x=30, y=115)
        switch_door_no.place(x=150, y=115)
    def client_exit_yes(self):
        global change
        change = "Yes"
        root.destroy()
        return change

    def client_exit_no(self):
        global change
        change = "No"
        root.destroy()
        return change

root = Tk()
root.geometry("200x200")
app = Window(root)
root.mainloop()


# Next Changing the Door and determining if the user has won
if change == 'Yes':
    y = 0
    while y == 0:
        for n in (1,2,3):
            if n != reveal and n != player_choice:
                player_choice = n
                y = 1
if player_choice == winning_door:
    win = "You Are a Winner!"
else:
    win = "Better Luck Next Time"
#The Final Frame for Display Game Results
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Monty Hall Door Game")
        self.pack(fill=BOTH, expand=1)

        L1 = Label(self, text="Your Final Door Selection is...")
        L1.place(x=20,y=30)
        L2 = Label(self, text="The Winning Door is...")
        L2.place(x=50, y=65)
        L3 = Label(self, text=player_choice)
        L3.place(x=90, y=50)
        L4 = Label(self, text=winning_door)
        L4.place(x=90, y=90)
        L5 = Label(self, text=win)
        L5.place(x=50, y=115)

root = Tk()
root.geometry("200x200")
app = Window(root)
root.mainloop()

