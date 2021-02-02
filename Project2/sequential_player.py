"""
test
"""


import random
from player import Player
from action import Action


class SequentialPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.counter = 0

    def select_action(self):
        counter_mod_3 = self.counter % 3
        value = self.action_map[counter_mod_3]
        self.counter += 1
        return Action(value)

    def receive_result(self, action):
        pass
