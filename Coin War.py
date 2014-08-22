# Copyright (c) 2014 Justin Blackmon
# Coin War game
# Compare the coins between two different players, determine the winner
# 5 coins per player
# Heads beats tails

import random

# Choice on whether the user wants random coins, or choose their own
choice = int(input("Press 1 to manually enter coins, or 2 for random. "))

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

# Generating the coin sequence
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
input("Press enter to proceed. ")

# Main game loop    
while len(player_1_army)!= 0 and len(player_2_army) != 0:
    
    # Print player status/ prompts
    print("Player 1:", player_1_army," ", player_1_prisoners)
    print("Player 2:", player_2_army," ", player_2_prisoners)
    input("\nPress enter to proceed to next round.\n ")
    
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
print("Player 1:", player_1_army," ", player_1_prisoners)
print("Player 2:", player_2_army," ", player_2_prisoners)
print("\nGame Over:\n")

# Printing the winners name
if len(player_1_army) == 0 and len(player_2_army) != 0:
    print("Player 2 wins!")
elif len(player_2_army) == 0 and len(player_1_army) !=0:
    print("Player 1 wins!")
    
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



input("\nPress enter to to exit. ")
