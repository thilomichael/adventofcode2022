# %% ===

with open("input.txt", "r") as f:
    input_str = f.read()

treemap = []
for row in input_str.strip().split("\n"):
    treemap.append([int(a) for a in row])

# %%

height = len(treemap)
width = len(treemap[0])
# print(height, width)


def is_visible(x, y):
    tree_height = treemap[x][y]
    # Upwards
    c = y - 1
    flag = False
    while c >= 0:
        if treemap[x][c] >= tree_height:
            flag = True
            break
        c -= 1
    if not flag:
        return True
    flag = False
    # Downwards
    c = y + 1
    while c < height:
        if treemap[x][c] >= tree_height:
            flag = True
            break
        c += 1
    if not flag:
        return True
    flag = False
    # Left
    c = x - 1
    while c >= 0:
        if treemap[c][y] >= tree_height:
            flag = True
            break
        c -= 1
    if not flag:
        return True
    flag = False
    # Right
    c = x + 1
    while c < width:
        if treemap[c][y] >= tree_height:
            flag = True
            break
        c += 1
    if not flag:
        return True
    return False


counter = 0
for x in range(width):
    for y in range(height):
        if is_visible(x, y):
            counter += 1
print(counter)

# %% ===

height = len(treemap)
width = len(treemap[0])


def scenic_score(x, y):
    tree_height = treemap[x][y]
    # Upwards
    c = y - 1
    up_score = 0
    while c >= 0:
        up_score += 1
        if treemap[x][c] >= tree_height:
            break
        c -= 1

    # Downwards
    c = y + 1
    down_score = 0
    while c < height:
        down_score += 1
        if treemap[x][c] >= tree_height:
            break
        c += 1
    # Left
    c = x - 1
    left_score = 0
    while c >= 0:
        left_score += 1
        if treemap[c][y] >= tree_height:
            break
        c -= 1
    # Right
    c = x + 1
    right_score = 0
    while c < width:
        right_score += 1
        if treemap[c][y] >= tree_height:
            break
        c += 1
    return up_score * down_score * left_score * right_score


max_scenic_score = 0
max_x = 0
max_y = 0
for x in range(width):
    for y in range(height):
        current_scenic_score = scenic_score(x, y)
        if current_scenic_score > max_scenic_score:
            max_scenic_score = current_scenic_score
            max_x = x
            max_y = y
print(max_scenic_score, f"at ({max_x}, {max_y})")
# %%
