"""
test
"""


import random
from player import Player
from action import Action


class HistorianPlayer(Player):
    def __init__(self, name, remember):
        super().__init__(name)
        self.history = []
        self.remember = remember
        self.is_beaten_by = {
            "rock": "paper",
            "paper": "scissor",
            "scissor": "rock"
        }

    def select_action(self):
        most_common_moves = {
          "rock": 0,
          "paper": 0,
          "scissor": 0
        }
        n_last_sequence = self.history[-self.remember:]

        # Returns a random value if the history is empty
        if len(n_last_sequence) == 0:
            random_value = random.randint(0, 2)
            value = self.action_map[random_value]
            return Action(value)

        for i in range(len(self.history)):
            temp_list = self.history[i:i + len(n_last_sequence)]
            if temp_list == n_last_sequence:
                return

    def receive_result(self, action):
        self.history.append[action.value]
