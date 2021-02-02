import matplotlib.pyplot as plt

player1 = [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
player2 = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]

rounds = [i for i in range(1, len(player1) + 1)]
player1_win_percentage = [sum(player1[:i]) / i for i in range(1, len(player1) + 1)]
player2_win_percentage = [sum(player2[:i]) / i for i in range(1, len(player2) + 1)]

plt.plot(rounds, player1_win_percentage)
plt.plot(rounds, player2_win_percentage)
plt.ylim(0, 1)
plt.title("Win rates")
plt.xlabel("x - Round")
plt.ylabel("y - %")
plt.show()