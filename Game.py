
from tkinter import *
import random
PlayerChoice = None

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
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
        Door1Button = Button(self, text="Door One", command= self.client_exit1)
        Door2Button = Button(self, text="Door Two", command= self.client_exit2)
        Door3Button = Button(self, text="Door Three", command= self.client_exit3)
        # placing the button on my window
        Door1Button.place(x=60, y=80)
        Door2Button.place(x=60, y=110)
        Door3Button.place(x=55, y=140)
    def client_exit1(self):
        global PlayerChoice
        PlayerChoice = 1
        root.destroy()
        return PlayerChoice

    def client_exit2(self):
        global PlayerChoice
        PlayerChoice = 2
        root.destroy()
        return PlayerChoice

    def client_exit3(self):
        global PlayerChoice
        PlayerChoice = 3
        root.destroy()
        return PlayerChoice


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("200x200")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
change = None
winningDoor = random.randint(1,3)
def doorrevealer(Choice,win):
    x = 0
    while x == 0:
        n = random.randint(1,3)
        if n != Choice and n != win:
            x = 1
            return n
reveal = doorrevealer(PlayerChoice,winningDoor)
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

        L1 = Label(self, text="I will Now Show you a Losing Door!")
        L1.place(x=5,y=30)
        L2 = Label(self, text="Door #......")
        L2.place(x=60, y=50)
        L3 = Label(self, text=reveal)
        L3.place(x=90, y=65)
        L4 = Label(self, text="Would You like to Change Doors?")
        L4.place(x=5, y=90)
        # creating a button instance
        SwitchDoorYes = Button(self, text="Yes", command= self.client_exit1a)
        SwitchDoorNo = Button(self, text="No", command= self.client_exit2a)
        # placing the button on my window
        SwitchDoorYes.place(x=30, y=115)
        SwitchDoorNo.place(x=150, y=115)
    def client_exit1a(self):
        global change
        change = "Yes"
        root.destroy()
        return change

    def client_exit2a(self):
        global change
        change = "No"
        root.destroy()
        return change


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("200x200")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
if change == 'Yes':
    y = 0
    while y == 0:
        for n in (1,2,3):
            if n != reveal and n != PlayerChoice:
                PlayerChoice = n
                y = 1
if PlayerChoice == winningDoor:
    Win = "You Are a Winner!"
else:
    Win = "Better Luck Next Time"
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

        L1 = Label(self, text="Your Final Door Selection is...")
        L1.place(x=20,y=30)
        L2 = Label(self, text="The Winning Door is...")
        L2.place(x=50, y=65)
        L3 = Label(self, text=PlayerChoice)
        L3.place(x=90, y=50)
        L4 = Label(self, text=winningDoor)
        L4.place(x=90, y=90)
        L5 = Label(self, text=Win)
        L5.place(x=50, y=115)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("200x200")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
