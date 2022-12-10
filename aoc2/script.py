# %% ==

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors

# Rock = 1 point, Paper = 2 points, Scissors = 3 points

opponent_moves = {"A": 1, "B": 2, "C": 3}
your_moves = {"X": 1, "Y": 2, "Z": 3}

# 3 beats 2, 2 beats 1, 1 beats 3


with open("input.txt", "r") as f:
    overall_score = 0
    for row in f.readlines():
        moves = row.strip().split(" ")
        opponent_move = opponent_moves[moves[0]]
        your_move = your_moves[moves[1]]
        print(f"{opponent_move} {your_move}")

        shape_score = your_move

        round_score = 0
        if opponent_move == your_move:  # draw
            round_score = 3
        elif (
            (your_move == 3 and opponent_move == 2)
            or (your_move == 2 and opponent_move == 1)
            or (your_move == 1 and opponent_move == 3)
        ):
            round_score = 6

        print("round score", round_score)

        overall_score += shape_score + round_score
    print(overall_score)
print("")

# %% ==

# X = lose, Y = draw, Z = win
# 1 = lose, 2 = draw, 3 = win

# 3 beats 2, 2 beats 1, 1 beats 3

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors

opponent_moves = {"A": 1, "B": 2, "C": 3}
results = {"X": 0, "Y": 3, "Z": 6}

with open("input.txt", "r") as f:
    overall_score = 0
    for row in f.readlines():
        moves = row.strip().split(" ")
        opponent_move = opponent_moves[moves[0]]
        result = results[moves[1]]

        round_score = result

        if result == 3:  # draw
            shape_score = opponent_move
        elif result == 0:  # lose
            shape_score = opponent_move - 1
            if shape_score == 0:
                shape_score = 3
        elif result == 6:
            shape_score = opponent_move + 1
            if shape_score == 4:
                shape_score = 1

        overall_score += shape_score + round_score
    print(overall_score)

# %%
