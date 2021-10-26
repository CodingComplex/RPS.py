import random
import math


def play():
    user = input("Choose between rock 🥌, paper 🧻 and scissors ✂ .\n")
    user = user.lower()

    bot = random.choice(['rock', 'paper', 'scissors'])

    if user == bot:
        return 0, user, bot

    if player_won(user, bot):

        return 1, user, bot

    return -1, user, bot


def player_won(player, opponent):

    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
            or (player == 'paper' and opponent == 'rock'):
        return True
    return False


def play_best_of(w):

    player_wins = 0
    bot_wins = 0
    wins_necessary = math.ceil(w/2)

    while player_wins < wins_necessary and bot_wins < wins_necessary:
        result, user, bot = play()

        if result == 0:
            print('Tied up! You and your opponent have both chosen {}. \n'.format(user))

        elif result == 1:
            player_wins += 1
            print('You chose {} and your opponent chose {}. You won This round.\n'.format(user, bot))
        else:
            bot_wins += 1
            print('You chose {} and your opponent chose {}. You lost This Round.\n'.format(user, bot))

    if player_wins > bot_wins:
        print('Congratulations! You have won the best of {} games!'.format(w))
    else:
        print('Unfortunately, your opponent has won the best of {} games. Better luck next time!'.format(w))


if __name__ == '__main__':
    play_best_of(5)
