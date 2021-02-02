"""
Test
"""

from tournament import Tournament
from random_player import RandomPlayer

TYPE_TO_CLASS_MAP = {
    "random": RandomPlayer
}


def main():
    print("Welcome to this game")

    player1_name = 'm' # input("Player 1, enter your name!: ")
    player1_type = 'random' # input("Player 1, enter your type!: ")
    player1_class = TYPE_TO_CLASS_MAP[player1_type.lower()]
    player1 = player1_class(player1_name)

    player2_name = 'n' # input("Player 2, enter your name!: ")
    player2_type = 'random' # input("Player 2, enter your type!: ")
    player2_class = TYPE_TO_CLASS_MAP[player2_type.lower()]
    player2 = player2_class(player2_name)

    num_games = 1 # input("Enter number of games to be played: ")

    tourny = Tournament(player1, player2, num_games)
    tourny.arrange_single_game()


main()
