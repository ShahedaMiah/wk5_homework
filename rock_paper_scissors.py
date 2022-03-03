import random
# random module imported so we can generate the computer's random play

def is_a_win(player, computer):
# function to return if player wins - set out the parameters for when the player wins
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    else:
        return False

def play_game():
    player = input("Enter your choice 'r' for rock, 'p' for paper, 's' for scissors:\n ").lower()
    # use '.lower()' to eliminate issues of lower/uppercase usage

    computer = random.choice(['r', 'p', 's'])
    # use 'random.choice' to randomly choose from the three options r, p and s

    if player == computer:
        print("You and the Computer both chose {}.\nIt was a tie".format(player, computer))
    elif is_a_win(player, computer):
    # set the 'is_a_win' function as the parameter for the winning 'if'
        print("You chose {} and the Computer chose {}.\nYou won this game! ".format(player, computer))
    else:
        print("You chose {} and the Computer chose {}.\nYou lost this game! ".format(player, computer))


def continuous_play_game():
# function which creates a loop so you can automatically continue to play game
    continue_to_play = 'y'
    while continue_to_play == 'y':
        play_game()
        continue_to_play = input("Do you want to play again? 'y' for yes and 'n' for no: \n").lower()
    else:
        return("Thank you for playing. See you next time!")

print(continuous_play_game())