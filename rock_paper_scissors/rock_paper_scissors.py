"""

Rock paper scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V).
It has only two possible outcomes: a draw, or a win for one player and a loss for the other.
A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors") but will lose to one who has played paper ("paper covers rock")
A play of paper will lose to a play of scissors ("scissors cuts paper")
If both players choose the same shape, the game is tied

"""

call_1, call_2 = input().split()

win_over = {
    "ROCK": "SCISSORS",
    "SCISSORS": "PAPER",
    "PAPER": "ROCK"
}

if call_1 != call_2:
    print('PLAYER1' if win_over[call_1] == call_2 else 'PLAYER2')
else:
    print('DRAW')