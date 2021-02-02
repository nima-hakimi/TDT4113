"""
test
"""


from player import Player
from action import Action


class MostCommonPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.previous_moves = {
          "rock": 0,
          "paper": 0,
          "scissor": 0
        }
        self.is_beaten_by = {
            "rock": "paper",
            "paper": "scissor",
            "scissor": "rock"
        }

    def select_action(self):
        most_common_move = ""
        number_of_common_moves = -1
        for key in self.previous_moves:
            if self.previous_moves[key] > number_of_common_moves:
                number_of_common_moves = self.previous_moves[key]
                most_common_move = key
        return Action(self.is_beaten_by[most_common_move])

    def receive_result(self, action):
        self.previous_moves[action.value] += 1
