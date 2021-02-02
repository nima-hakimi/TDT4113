"""
test
"""


class SingleGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def perform_game(self):
        action1 = self.player1.select_action()
        action2 = self.player2.select_action()
        self.player1.receive_result(action2)
        self.player2.receive_result(action1)
        if action1 > action2:
            self.show_result(self.player1, action1, action2)
            return "player1"
        elif action2 > action1:
            self.show_result(self.player2, action1, action2)
            return "player2"
        self.show_result(None, action1, action2)
        return None

    def show_result(self, winner, action1, action2):
        general_str = "%s: %s. %s: %s --> " % (self.player1.name, action1.value, self.player2.name, action2.value)
        if winner is None:
            print(general_str + "TIE!")
        else:
            print(general_str + "%s WINS!" % winner.name)
