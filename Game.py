from tkinter import *
import random
def door_revealer(choice,win):
    '''This function helps decide which door is revealed to not be the winning door to our player.
    In the situation where the winning door and the chosen door are different, there is only one possible door it can reveal.
    However, in the situation where the winning door is the chosen door, it must select one of two doors to reveal, in this use case
    we need it to select the reveal door randomly'''
    x = 0
    while x == 0:
        n = random.randint(1,3)
        if n != choice and n != win:
            x = 1
            return n
def change_door_func(revealed_door,play_choice):
  '''This function is a quick way to select the door that is not the revealed door and not the players original choice'''
  for n in (1,2,3):
      if n != revealed_door and n != play_choice:
          return n
"""Here, we are creating our three window classes for the three windows that will be utilized during the game 
and inheriting from the Frame class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
This initial Window is for the player to select the door, there will be two more frames, one for the reveal
and a final frame to announce the results of the game """
class door_selection_window(Frame):
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
        self.choice = None
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
        # Global variables can be found used below. Though in all normal circumstances, I would avoid using Global variables.
        # Given Python's lack of event based programming, I was not able to find an alternative to store the player choice from the button click function
    def client_exit1(self):
        '''This function is for closing the first window with a player selection of the first door'''
        self.choice = 1
        root.destroy()
    def client_exit2(self):
        '''This function is for closing the first window with a player selection of the second door'''
        self.choice = 2
        root.destroy()
    def client_exit3(self):
        '''This function is for closing the first window with a player selection of the third door'''
        self.choice = 3
        root.destroy()
# This is now our second Window, Extremely similar to the first, just different Text Show to the user, and different buttons
class reveal_window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Monty Hall Door Game")
        self.pack(fill=BOTH, expand=1)
        self.change = None
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
        self.change = "Yes"
        root.destroy()
    def client_exit_no(self):
        self.change = "No"
        root.destroy()
# The Third Window is unique it has no selections to be made on it. Solely The results.
class result_window(Frame):
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
if __name__ == "__main__":
    # we start by setting our window size and running our first option window
    root = Tk()
    root.geometry("200x200")
    door_selection_window_var = door_selection_window(root)
    root.mainloop()
    #Now we take the placer choice and select a door to reveal to the player
    player_choice = door_selection_window_var.choice
    '''This line calls the door selection from the first branch to the main scope'''
    winning_door = random.randint(1, 3)
    '''This line randomly selects which door is the winning door.'''
    reveal = door_revealer(player_choice, winning_door)
    '''reveal is now in this line storing the variable result from the door_revealer function  It must do so before the second window is made.
    Now that we have chosen a door to reveal to the player we can go to the next window'''
    root = Tk()
    root.geometry("200x200")
    reveal_window_var = reveal_window(root)
    root.mainloop()
    '''After this window, the user has now chosen whether or not they would like to change doors.  Their selection was stored in the change function
    Next Changing the Door and determining if the user has won'''
    if reveal_window_var.change == 'Yes':
        player_choice = change_door_func(reveal,player_choice)
    if player_choice == winning_door:
        win = "You Are a Winner!"
    else:
        win = "Better Luck Next Time"
    # The Final Frame for Displaying Game Results is Called Now
    root = Tk()
    root.geometry("200x200")
    result_window_var = result_window(root)
    root.mainloop()
