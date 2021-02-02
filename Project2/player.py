"""
test
"""


class Player:
    """ Super class. """
    def __init__(self, name):
        self.name = name
        self.action_map = {
            0: "rock",
            1: "paper",
            2: "scissor"
        }

    def change_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
