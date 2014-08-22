# Coin War game
# Compare the coins between two different players, determine the winner
# 5 coins per player
# Heads beats tails

import random
from tkinter import *

# Choice on whether the user wants random coins, or choose their own
#choice = int(input("Press 1 to manually enter coins, or 2 for random. "))

# Variable list
coin_list = ("H", "T", "h", "t")
player_1_army = []
player_1_prisoners = []
player_2_prisoners = []
player_2_army = []
player_1_count = 0
player_2_count = 0
random_army_1 = [random.choice("HT") for i in range(5)]
random_army_2 = [random.choice("HT") for i in range(5)]

class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        global player_1_army
        global player_2_army
        Label(self,
              text = "Random or Manual entry:"
              ).grid(row = 1, column = 0, sticky = W)
        self.choice = StringVar()
        self.choice.set(None)
        
        Radiobutton(self,
                    text = "Manual coins",
                    variable = self.choice,
                    value = "1",
                    command = self.coin_choice
                    ).grid(row = 2, column = 0, sticky = W)
        Radiobutton(self,
                    text = "Random coins",
                    variable = self.choice,
                    value = "2",
                    command = self.coin_choice
                    ).grid(row = 2, column = 1, sticky = W)
        Label(self,
              text = "Player 1, enter 5 coins(H, T): "
              ).grid(row = 3, column = 0, sticky = W)
        self.player_1_army = Entry(self)
        self.player_1_army.grid(row = 4, column = 0, sticky = W)
        
        Label(self,
              text = "Player 2, enter 5 coins(H, T): "
              ).grid(row = 5, column = 0, sticky = W)
        self.player_2_army = Entry(self)
        self.player_2_army.grid(row = 6, column = 0, sticky = W)

        Button(self,
               text = "Click to play the game",
               command = self.game_loop
               ).grid(row = 7, column = 0, sticky = W)
        
        self.game_txt = Text(self, width = 45, height = 10, wrap = WORD)
        self.game_txt.grid(row = 7, column = 2, columnspan = 2)
# Generating the coin sequence
    def coin_choice(self):
        choice = self.choice.get()
        global player_1_army 
        global player_1_prisoners 
        global player_2_prisoners 
        global player_2_army 
        global player_1_count 
        global player_2_count 
        global random_army_1 
        global random_army_2 
        while choice == 1:
   
            while player_1_count <= 4:
                player_1_choice = input("Player 1 enter an H or a T: ")
                player_1_choice = player_1_choice.upper()
                if player_1_choice not in coin_list:
                    print("That is not an H or a T")
                else:
                    player_1_count +=1
                    player_1_army += player_1_choice 
            while player_2_count <= 4:
                player_2_choice = input("Player 2 enter an H or a T: ")
                player_2_choice = player_2_choice.upper()
                if player_2_choice not in coin_list:
                    print("That is not an H or a T")
                else:
                    player_2_count +=1
                    player_2_army += player_2_choice
            print("\nYour respective armies are:\n""Player 1:", player_1_army,"\n"\
                   "Player 2:", player_2_army)
            break
        while choice == 2:
            player_1_army = random_army_1
            player_2_army = random_army_2
            print(player_1_army)
            print(player_2_army)
            break
        #input("Press enter to proceed. ")
    def start(self):
        starting = "Player 1:", player_1_army, player_1_prisoners,
        "Player 2:", player_2_army, player_2_prisoners
        
        
      

# Main game loop
    def game_loop(self):
        global coin_list 
        global player_1_army 
        global player_1_prisoners
        global player_2_prisoners
        global player_2_army
        global player_1_count 
        global player_2_count
        global random_army_1
        global random_army_2 
        while len(player_1_army)!= 0 and len(player_2_army) != 0:
    
            # Print player status/ prompts
            print("Player 1:", player_1_army," ", player_1_prisoners)
            print("Player 2:", player_2_army," ", player_2_prisoners)
            #input("\nPress enter to proceed to next round.\n ")
            self.game_txt.insert(0.0, game_loop)
            # Tie    
            if player_1_army[0] == "H" and player_2_army[0] == "H":
                if len(player_1_army) == 1 or len(player_2_army) == 1:
                    player_1_prisoners.append(player_1_army.pop(0))
            
                    player_2_prisoners.append(player_2_army.pop(0))
                    break
                for i in range(2):
                        player_1_prisoners.append(player_1_army.pop(0))
                        player_2_prisoners.append(player_2_army.pop(0))
            # Tie    
            elif player_1_army[0] == "T" and player_2_army[0] == "T":
                if len(player_1_army) == 1 or len(player_2_army) == 1:
                    player_1_prisoners.append(player_1_army.pop(0))
            
                    player_2_prisoners.append(player_2_army.pop(0))
                    break
                for i in range(2):
                        player_1_prisoners.append(player_1_army.pop(0))
                        player_2_prisoners.append(player_2_army.pop(0))
                
            # Player 1 win    
            elif player_1_army[0] == "H" and player_2_army[0] == "T":
                player_1_army.append(player_2_army.pop(0))
                player_1_army.append(player_1_army.pop(0))
                player_1_army.extend(player_2_prisoners)
                player_1_army.extend(player_1_prisoners)
                del(player_2_prisoners[:])
                del(player_1_prisoners[:])
        
            # Player 2 wins    
            elif player_1_army[0] == "T" and player_2_army[0] == "H":
                player_2_army.append(player_1_army.pop(0))
                player_2_army.append(player_2_army.pop(0))
                player_2_army.extend(player_1_prisoners)
                player_2_army.extend(player_2_prisoners)
                del(player_1_prisoners[:])
                del(player_2_prisoners[:])

    # Printing once a game is finished       
    #print("Player 1:", player_1_army," ", player_1_prisoners)
    ##print("Player 2:", player_2_army," ", player_2_prisoners)
   # print("\nGame Over:\n")

        # Printing the winners name
    if len(player_1_army) == 0 and len(player_2_army) != 0:
        #print("Player 2 wins!")
    #elif len(player_2_army) == 0 and len(player_1_army) !=0:
        #print("Player 1 wins!")
    
        # This loop starts if both players have no army    
        while len(player_1_army)== 0 and len(player_2_army) == 0:
            player_1_H = player_1_prisoners.count("H")
            player_2_H = player_2_prisoners.count("H")
    
            if player_1_H > player_2_H:
                print("Player 1 wins")
            elif player_1_H < player_2_H:
                print("Player 2 wins")
            elif player_1_H == player_2_H:
                print("It's a draw")
            break
    def tell_story(self):
        starting = self.start.get()
        self.game_txt.insert(0.0, starting)


#input("\nPress enter to to exit. ")

root = Tk()
root.title("Coin War")
app = Application(root)
root.mainloop()
