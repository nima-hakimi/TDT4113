"""
test
"""


class Action:
    """ ruh """
    def __init__(self, value):
        self.value = value
        self.beats = {
            "rock": "scissor",
            "scissor": "paper",
            "paper": "rock"
        }

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        if self.beats[self.value] == other.value:
            return True
        return False
