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
        n_last_sequence = self.history[-self.remember:]
        for i in range(len(self.history)):
            temp_list = self.history[i:i + len(n_last_sequence)]
            if temp_list == n_last_sequence:
                #Add self.history[i + len(n_last_sequence) + 1]


    def receive_result(self, action):
        self.history.append[action.value]
