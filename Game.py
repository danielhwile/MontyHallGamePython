from tkinter import *
try:
    from PIL import Image, ImageTk
except ModuleNotFoundError:
    import Image
except:
    print(f'Error: Could not import')
import matplotlib.pyplot as plt
import random
import csv

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

        #Creating our Text Labels
        title_label = Label(self, text="Please Select a Door!")

        #loading our images
        load = Image.open("./images/door2comp.png")
        render = ImageTk.PhotoImage(load)

        #assigning our door images
        door1_img = Label(self, image=render)
        door2_img = Label(self, image=render)
        door3_img = Label(self, image=render)
        door1_img.image = render
        door2_img.image = render
        door3_img.image = render

        # creating our button instances
        door1_button = Button(self, text="Door One", command= self.client_exit1)
        door2_button = Button(self, text="Door Two", command= self.client_exit2)
        door3_button = Button(self, text="Door Three", command= self.client_exit3)

        # placing the objects in our window
        title_label.place(x=95, y=15)
        #door 1
        door1_img.place(x=10, y=100)
        door1_button.place(x=8, y=195)
        #door 2
        door2_img.place(x=110, y=100)
        door2_button.place(x=108, y=195)
        #door 3
        door3_img.place(x=210, y=100)
        door3_button.place(x=207, y=195)

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

        L1 = Label(self, text="I'm a nice guy! So as a nice guy, I want to help you...\n I will show you one of the losing doors...")
        L1.place(x=5,y=5)
        L2 = Label(self, text="Door #"+str(reveal)+" Is not the winning door.")
        L2.place(x=60, y=45)
        L3 = Label(self, text="Your Door")

        L4 = Label(self, text="Would You like to Change your Door selection\n to door #"+str(not_reveal)+"?")
        L4.place(x=25, y=215)

        plaindoor = Image.open("./images/door2comp.png")
        plain_door_render = ImageTk.PhotoImage(plaindoor)
        chosendoor = Image.open("./images/doorcomp.png")
        chosen_door_render = ImageTk.PhotoImage(chosendoor)
        elimdoor = Image.open("./images/elimdoorcomp.png")
        elim_door_render = ImageTk.PhotoImage(elimdoor)

        #assigning our door images
        door1_img = Label(self, image=plain_door_render)
        door2_img = Label(self, image=plain_door_render)
        door3_img = Label(self, image=plain_door_render)
        door1_img.image = plain_door_render
        door2_img.image = plain_door_render
        door3_img.image = plain_door_render
        if player_choice == 1:
            door1_img = Label(self, image=chosen_door_render)
            door1_img.image = chosen_door_render
        elif player_choice == 2:
            door2_img = Label(self, image=chosen_door_render)
            door2_img.image = chosen_door_render
        else:
            door3_img = Label(self, image=chosen_door_render)
            door3_img.image = chosen_door_render
        if reveal == 1:
            door1_img = Label(self, image=elim_door_render)
            door1_img.image = elim_door_render
        elif reveal == 2:
            door2_img = Label(self, image=elim_door_render)
            door2_img.image = elim_door_render
        else:
            door3_img = Label(self, image=elim_door_render)
            door3_img.image = elim_door_render


        # placing the objects in our window
        #door 1
        door1_img.place(x=10, y=100)
        #door 2
        door2_img.place(x=110, y=100)
        #door 3
        door3_img.place(x=210, y=100)
        if player_choice == 1:
            L3.place(x=10, y=195)
        elif player_choice == 2:
            L3.place(x=110, y=195)
        else:
            L3.place(x=210, y=195)

        switch_door_yes = Button(self, text="Yes", command= self.client_exit_yes)
        switch_door_no = Button(self, text="No", command= self.client_exit_no)

        switch_door_yes.place(x=75, y=255)
        switch_door_no.place(x=185, y=255)
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

        self.graph = 0
        self.replay = 0

        replay = Button(self, text="Replay?", command=self.client_replay)
        replay.place(x=75, y=135)

        display_graphic = Button(self, text="Display Results Graphic", command=self.client_graph)
        display_graphic.place(x=35, y=165)
    def client_replay(self):
        self.replay = 1
        root.destroy()
    def client_graph(self):
        self.replay = 1
        self.graph = 1
        root.destroy()


if __name__ == "__main__":
    # we start by setting our window size and running our first option window
    x = 1
    while x == 1:
        x = 2
        root = Tk()
        root.geometry("300x300")
        door_selection_window_var = door_selection_window(root)
        root.mainloop()

        if door_selection_window_var.choice == None:
            sys.exit(0)
        #This line is to close out the game if the user closes out the window rather than enter a decision.

        #Now we take the placer choice and select a door to reveal to the player
        player_choice = door_selection_window_var.choice
        '''This line calls the door selection from the first branch to the main scope'''
        winning_door = random.randint(1, 3)
        '''This line randomly selects which door is the winning door.'''
        reveal = door_revealer(player_choice, winning_door)
        if reveal != 1 and player_choice !=1:
            not_reveal = 1
        if reveal != 2 and player_choice !=2:
            not_reveal = 2
        if reveal !=3 and player_choice !=3:
            not_reveal = 3
        '''reveal is now in this line storing the variable result from the door_revealer function  It must do so before the second window is made.
        Now that we have chosen a door to reveal to the player we can go to the next window'''
        root = Tk()
        root.geometry("300x300")
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
        data = []
        with open('./Record/Records.csv', 'r') as c:
            s = csv.reader(c, delimiter=',')
            for row in s:
                data.append(row)
        if reveal_window_var.change == 'Yes':
            data[-1][0] = int(data[-1][0])
            data[-1][0] += 1
        else:
            data[-1][2] = int(data[-1][2])
            data[-1][2] +=1
        if reveal_window_var.change == 'Yes' and player_choice == winning_door:
            data[-1][1] = int(data[-1][1])
            data[-1][1] +=1
        elif player_choice == winning_door:
            data[-1][3] = int(data[-1][3])
            data[-1][3] += 1
        if result_window_var.graph == 1:
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Wins', 'Loses'
            ax1data = []
            ax1data.append(int(data[-1][1]))
            ax1data.append((int(data[-1][0])-int(data[-1][1])))
            ax2data = []
            ax2data.append(int(data[-1][3]))
            ax2data.append(int((data[-1][2]))-int(data[-1][3]))
            explode = (0.1, 0)

            fig, (ax1, ax2) = plt.subplots(1, 2)
            ax1.pie(ax1data, colors=['g','r'],explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            ax2.pie(ax2data, colors=['g','r'],explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            ax1.set_title('Results With Changing Door')
            ax2.set_title('Results Without Changing Door')
            plt.show()
        with open('./Record/Records.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data[-1])


        if result_window_var.replay == 1:
            x = 1
