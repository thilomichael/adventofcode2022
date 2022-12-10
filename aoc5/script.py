# %% ===

positions = []
moves = []
with open("input.txt", "r") as f:
    emptyline = False
    for row in f.readlines():
        r = row.replace("\n", "")
        if r == "":
            emptyline = True
            continue

        if not emptyline:
            positions.append(r)
        else:
            moves.append(r)

stacks = []
for column in range(9):
    current_column = []
    for row in range(len(positions) - 1):
        current_row = positions[row]
        element = current_row[1 + (4 * column)]
        if element != " ":
            current_column.append(element)
    current_column.reverse()
    stacks.append(current_column)


def print_stack(stacks):
    for column in stacks:
        for element in column:
            print(element, " ", end="")
        print()


for move in moves:
    move_split = move.split(" ")
    multiplicator = int(move_split[1])
    from_pos = int(move_split[3]) - 1
    to_pos = int(move_split[5]) - 1
    # print(multiplicator, from_pos, to_pos)

    for i in range(multiplicator):
        element = stacks[from_pos].pop()
        stacks[to_pos].append(element)

print_stack(stacks)

answer = ""
for column in stacks:
    answer += column[-1]
print(answer)

# %% ===

positions = []
moves = []
with open("input.txt", "r") as f:
    emptyline = False
    for row in f.readlines():
        r = row.replace("\n", "")
        if r == "":
            emptyline = True
            continue

        if not emptyline:
            positions.append(r)
        else:
            moves.append(r)

stacks = []
for column in range(9):
    current_column = []
    for row in range(len(positions) - 1):
        current_row = positions[row]
        element = current_row[1 + (4 * column)]
        if element != " ":
            current_column.append(element)
    current_column.reverse()
    stacks.append(current_column)


def print_stack(stacks):
    for column in stacks:
        for element in column:
            print(element, " ", end="")
        print()


for move in moves:
    move_split = move.split(" ")
    multiplicator = int(move_split[1])
    from_pos = int(move_split[3]) - 1
    to_pos = int(move_split[5]) - 1
    # print(multiplicator, from_pos, to_pos)

    # print(stacks[from_pos], multiplicator)
    new_list = []
    for i in range(multiplicator):
        new_list.append(stacks[from_pos].pop())
    new_list.reverse()
    stacks[to_pos].extend(new_list)

print_stack(stacks)

answer = ""
for column in stacks:
    answer += column[-1]
print(answer)

# %%
