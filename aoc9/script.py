# %% ==

with open("input.txt", "r") as f:
    input_str = f.read()

commands = input_str.strip().split("\n")
commands = [x.split(" ") for x in commands]
commands = [(x[0], int(x[1])) for x in commands]
commands

# %% ===

hx, tx, hy, ty = 0, 0, 0, 0
visited = []

for direction, steps in commands:
    for i in range(steps):

        if direction == "U":  # up
            hy += 1
        elif direction == "D":  # down
            hy -= 1
        elif direction == "L":  # left
            hx -= 1
        elif direction == "R":  # right
            hx += 1

        dx = hx - tx
        dy = hy - ty

        if dx == 2:
            tx += 1
            if dy == 1:
                ty += 1
            elif dy == -1:
                ty -= 1
        elif dx == -2:
            tx -= 1
            if dy == 1:
                ty += 1
            elif dy == -1:
                ty -= 1
        elif dy == 2:
            ty += 1
            if dx == 1:
                tx += 1
            elif dx == -1:
                tx -= 1
        elif dy == -2:
            ty -= 1
            if dx == 1:
                tx += 1
            elif dx == -1:
                tx -= 1

        visited.append((tx, ty))

print(len(set(visited)))

# %% ==

rx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ry = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
visited = []

for direction, steps in commands:
    for i in range(steps):

        if direction == "U":  # up
            ry[0] += 1
        elif direction == "D":  # down
            ry[0] -= 1
        elif direction == "L":  # left
            rx[0] -= 1
        elif direction == "R":  # right
            rx[0] += 1

        for i in range(1, len(rx)):
            dx = rx[i - 1] - rx[i]
            dy = ry[i - 1] - ry[i]

            if dx == 2:
                rx[i] += 1
                if dy >= 1:
                    ry[i] += 1
                elif dy <= -1:
                    ry[i] -= 1
            elif dx == -2:
                rx[i] -= 1
                if dy >= 1:
                    ry[i] += 1
                elif dy <= -1:
                    ry[i] -= 1
            elif dy == 2:
                ry[i] += 1
                if dx >= 1:
                    rx[i] += 1
                elif dx <= -1:
                    rx[i] -= 1
            elif dy == -2:
                ry[i] -= 1
                if dx >= 1:
                    rx[i] += 1
                elif dx <= -1:
                    rx[i] -= 1

        visited.append((rx[-1], ry[-1]))

print(len(set(visited)))
# %%
