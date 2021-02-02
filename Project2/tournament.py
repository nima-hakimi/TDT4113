"""
test
"""


from single_game import SingleGame

class Tournament:
    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games
        self.player1_points = []
        self.player2_points = []

    def arrange_single_game(self):
        single_game = SingleGame(self.player1, self.player2)
        winner = single_game.perform_game()
        if winner is None:
            self.player1_points.append(0.5)
            self.player2_points.append(0.5)
        elif winner == "player1":
            self.player1_points.append(1)
            self.player2_points.append(0)
        elif winner == "player2":
            self.player1_points.append(0)
            self.player2_points.append(1)
        else:
            print("arrange_single_game() went wrong")



