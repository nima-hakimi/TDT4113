"""
test
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.action_map = {
            0: "rock",
            1: "paper",
            2: "scissor"
        }

    def change_name(self, name):
        self.name = name
