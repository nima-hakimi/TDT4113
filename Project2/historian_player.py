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
                if i + len(n_last_sequence) + 1 >= len(self.history):
                    break
                next_move = self.history[i + len(n_last_sequence) + 1]
                most_common_moves[next_move] += 1

        most_common_move = ""
        number_of_common_moves = -1
        for key in most_common_moves.keys():
            if most_common_moves[key] > number_of_common_moves:
                number_of_common_moves = most_common_moves[key]
                most_common_move = key
        return Action(self.is_beaten_by[most_common_move])

    def receive_result(self, action):
        self.history.append[action.value]
