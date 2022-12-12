# %% ===

with open("input.txt", "r") as f:
    input_text = f.read().strip().split("\n")

input_text

# %% ===
import math

height_map = []
start = (-1, -1)
end = (-1, -1)
for y, row in enumerate(input_text):
    curr_row = []
    for x, char in enumerate(list(row)):
        if char == "S":
            height = 0
            start = (y, x)
        elif char == "E":
            height = 27
            end = (y, x)
        else:
            height = ord(char) - 96
        curr_row.append(height)
    height_map.append(curr_row)

# print(height_map)
# print(start,end)
width = len(height_map[0])
height = len(height_map)

# steps to end
steps = [[math.inf for j in range(width)] for i in range(height)]
directions = [[None for j in range(width)] for i in range(height)]
options = [start, end]
# globally list of current options
# for each current option point
# steps to exit
# direction of travel (u,d,l,r)


def sort_condition(option):
    return steps[option[0]][option[1]]


def get_valid_neighbors(option):
    global options, steps, height_map
    steps_to_end = steps[option[0]][option[1]]
    up = (option[0] - 1, option[1])
    down = (option[0] + 1, option[1])
    left = (option[0], option[1] - 1)
    right = (option[0], option[1] + 1)
    option_height = height_map[option[0]][option[1]]

    valid_neighbors = []
    for n in [up, down, left, right]:
        # check for out of bounds
        if n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width:
            # check for height accessibility
            if option_height <= height_map[n[0]][n[1]] + 1:
                # check if already visited
                if steps[n[0]][n[1]] == math.inf:
                    valid_neighbors.append(n)
                    steps[n[0]][n[1]] = steps_to_end + 1

    return valid_neighbors


def set_direction(option):
    global options, steps, height_map
    steps_to_end = steps[option[0]][option[1]]
    up = (option[0] - 1, option[1])
    down = (option[0] + 1, option[1])
    left = (option[0], option[1] - 1)
    right = (option[0], option[1] + 1)
    option_height = height_map[option[0]][option[1]]

    valid_directions = []
    for n in [up, down, left, right]:
        # check for out of bounds
        if n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width:
            # check for height accessibility
            if option_height <= height_map[n[0]][n[1]] + 1:
                if steps[n[0]][n[1]] != math.inf:
                    valid_directions.append(n)
    if len(valid_directions) == 0:
        print("This should not happen")
    valid_directions.sort(key=sort_condition)
    if valid_directions[0] == up:
        directions[option[0]][option[1]] = "^"
    elif valid_directions[0] == down:
        directions[option[0]][option[1]] = "v"
    elif valid_directions[0] == left:
        directions[option[0]][option[1]] = "<"
    elif valid_directions[0] == right:
        directions[option[0]][option[1]] = ">"
    else:
        print("This cannot happen")


steps[end[0]][end[1]] = 0
while directions[start[0]][start[1]] is None:
    options.sort(key=sort_condition)
    curr_option = options.pop(0)
    neighbors = get_valid_neighbors(curr_option)
    options.extend(neighbors)
    set_direction(curr_option)

print(steps[start[0]][start[1]])

for y, row in enumerate(directions):
    for x, direction in enumerate(row):
        current_pos = (y, x)
        if current_pos == start:
            print("S", end="")
        elif current_pos == end:
            print("E", end="")
        elif direction == None:
            print(" ", end="")
        else:
            print(direction, end="")
    print()

# %% ===
import math

height_map = []
start = (-1, -1)
end = (-1, -1)
for y, row in enumerate(input_text):
    curr_row = []
    for x, char in enumerate(list(row)):
        if char == "S":
            height = 0
            start = (y, x)
        elif char == "E":
            height = 27
            end = (y, x)
        else:
            height = ord(char) - 96
        curr_row.append(height)
    height_map.append(curr_row)


width = len(height_map[0])
height = len(height_map)

steps = [[math.inf for j in range(width)] for i in range(height)]
directions = [[None for j in range(width)] for i in range(height)]
options = [start, end]


def sort_condition(option):
    return steps[option[0]][option[1]]


def get_valid_neighbors(option):
    global options, steps, height_map
    steps_to_end = steps[option[0]][option[1]]
    up = (option[0] - 1, option[1])
    down = (option[0] + 1, option[1])
    left = (option[0], option[1] - 1)
    right = (option[0], option[1] + 1)
    option_height = height_map[option[0]][option[1]]

    valid_neighbors = []
    for n in [up, down, left, right]:
        # check for out of bounds
        if n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width:
            # check for height accessibility
            if option_height <= height_map[n[0]][n[1]] + 1:
                # check if already visited
                if steps[n[0]][n[1]] == math.inf:
                    valid_neighbors.append(n)
                    steps[n[0]][n[1]] = steps_to_end + 1

    return valid_neighbors


def set_direction(option):
    global options, steps, height_map
    steps_to_end = steps[option[0]][option[1]]
    up = (option[0] - 1, option[1])
    down = (option[0] + 1, option[1])
    left = (option[0], option[1] - 1)
    right = (option[0], option[1] + 1)
    option_height = height_map[option[0]][option[1]]

    valid_directions = []
    for n in [up, down, left, right]:
        # check for out of bounds
        if n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width:
            # check for height accessibility
            if option_height <= height_map[n[0]][n[1]] + 1:
                if steps[n[0]][n[1]] != math.inf:
                    valid_directions.append(n)
    if len(valid_directions) == 0:
        print("This should not happen")
    valid_directions.sort(key=sort_condition)
    if valid_directions[0] == up:
        directions[option[0]][option[1]] = "^"
    elif valid_directions[0] == down:
        directions[option[0]][option[1]] = "v"
    elif valid_directions[0] == left:
        directions[option[0]][option[1]] = "<"
    elif valid_directions[0] == right:
        directions[option[0]][option[1]] = ">"
    else:
        print("This cannot happen")


steps[end[0]][end[1]] = 0
while len(options) > 0:
    options.sort(key=sort_condition)
    curr_option = options.pop(0)
    neighbors = get_valid_neighbors(curr_option)
    options.extend(neighbors)
    set_direction(curr_option)

min_steps = math.inf
for y in range(height):
    for x in range(width):
        if height_map[y][x] > 1:
            continue
        if steps[y][x] < min_steps:
            min_steps = steps[y][x]

min_steps
# %%
