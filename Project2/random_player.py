"""
test
"""


import random
from player import Player
from action import Action


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def select_action(self):
        random_value = random.randint(0, 2)
        value = self.action_map[random_value]
        return Action(value)

    def receive_result(self, action):
        pass
