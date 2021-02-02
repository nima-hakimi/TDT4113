"""
test
"""


from player import Player
from action import Action


class HistorianPlayer(Player):
    def __init__(self, name, remember):
        super().__init__(name)
        self.history = []
        self.remember = remember

    def select_action(self):


    def receive_result(self, action):
        self.history.append[action.value]
