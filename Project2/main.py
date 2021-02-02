"""
Test
"""


from tournament import Tournament
from random_player import RandomPlayer
from sequential_player import SequentialPlayer
from most_common_player import MostCommonPlayer
from historian_player import HistorianPlayer

TYPE_TO_CLASS_MAP = {
    "random": RandomPlayer,
    "seq": SequentialPlayer,
    "mc": MostCommonPlayer,
    "hist": HistorianPlayer
}


def main():
    print("Welcome to this game")

    player1_name = 'm'  # input("Player 1, enter your name!: ")
    player1_type = 'hist'  # input("Player 1, enter your type!: ")
    player1_class = TYPE_TO_CLASS_MAP[player1_type.lower()]

    if player1_type == 'hist':
        player1_remember = 1  # input("Player 1, enter remember value!: ")
        player1 = player1_class(player1_name, player1_remember)    
    else:
        player1 = player1_class(player1_name)

    player2_name = 'n'  # input("Player 2, enter your name!: ")
    player2_type = 'seq'  # input("Player 2, enter your type!: ")
    player2_class = TYPE_TO_CLASS_MAP[player2_type.lower()]

    if player2_type == 'hist':
        player2_remember = 1  # input("Player 2, enter remember value!: ")
        player2 = player2_class(player2_name, player2_remember)
    else:
        player2 = player2_class(player2_name)

    num_games = 100  # input("Enter number of games to be played: ")

    tourny = Tournament(player1, player2, num_games)
    tourny.arrange_tournament()

main()
