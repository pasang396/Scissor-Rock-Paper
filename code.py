# Scissor-Rock-Paper
# This is 1st python code via Kylie Ying.

import math
import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    return (1, user, computer) if is_win(user, computer) else (-1, user, computer)


def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r

    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')


def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)

    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:  # tie
            print(f'It is a tie. You and the computer have both chosen {user}. \n')

        elif result == 1:  # you win
            player_wins += 1
            print(f'You chose {user} and the computer chose {computer}. You won!\n')

        else:
            computer_wins += 1
            print(f'You chose {user} and the computer chose {computer}. You lost :(\n')

    if player_wins > computer_wins:
        print(f'You have won the best of {n} games! What a champ :D')

    else:
        print(f'Unfortunately, the computer has won the best of {n} games. Better luck next time!')


if __name__ == '__main__':
    play_best_of(3) # 2
