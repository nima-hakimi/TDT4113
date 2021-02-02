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

    def select_action(self):
        value = "rock"
        return Action(value)

    def receive_result(self, action):
        pass
