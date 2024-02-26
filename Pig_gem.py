"If you want to Know How the game work, Just go to the end of the code"

import random

# creating the rolling the dice from randamely
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll


# taking input as number of player and cheaking the validity
while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if (2 <= players <=4):
            break
        else:            
            print("Please enter the player btw 2 to 4: ")
    else:
        print("Invailid ! Try again")


# having a maximum score and creating a multiple player score
max_score = 30
player_score = [0 for _ in range(players)]

# cheaking if the player is want to roll the dice when player didn't reached the maximum score
while max(player_score) < max_score * players:

    # Traking score of each player (if two player then loop run two times and keep track of each player score)
    for player_inx in range(players):

        # we plus one becaouse the index start with zero
        print("\nplayer number",player_inx + 1, "Your tern just started")
        print("Your total score is",player_score[player_inx],"\n")
        current_score = 0

        # This loop help us to roll the dice for each player untill all the player run his tern
        while True:
            should_roll = input("Would you like to roll again (y): ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("\nyou rolled a 1: Game Over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a value: ",value)
            print("Your current score is ",current_score)

            # Check if the player's score exceeds or equals max_score
            if player_score[player_inx] + current_score >= max_score:
                break  # Exit the inner while loop


    # In the list of each player score we are showing the player score based on there player index
    # and adding the current score to that player   
        player_score[player_inx] += current_score
        print("your total score is",player_score[player_inx])


    # Check if any player's score exceeds or equals max_score
    if max(player_score) >= max_score:
        break  # Exit the outer while loop

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("The winner is player:",winning_idx + 1,
      "With the socre of ",max_score)


# Here is the discription of how the game works
"""Pig is a fun dice game for two or more players. The goal is to be the first 
player to reach a certain number of points (in this game is 50). On your turn, 
you roll a special six-sided die. If you roll a 1, you lose all the 
points you've collected so far this turn, and it's the next player's 
turn. But if you roll any other number, you get to add that number of 
points to your score for the turn. You can choose to keep rolling to 
try to get more points, or you can stop and keep the points you've 
earned so far. But be careful, if you keep rolling and roll a 1, you 
lose all the points for that turn! The game continues until one player 
reaches the winning score of 50 points. It's a game of luck, strategy, 
and knowing when to take risks!"""
