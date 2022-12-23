# %% ==

with open("input.txt", "r") as f:
    input_text = f.read().split("\n")

input_text

# %%

# Build the map
cave = {}

for row in input_text:
    edges = row.split(" -> ")
    for i in range(len(edges) - 1):
        current_xy = edges[i].split(",")  # current
        next_xy = edges[i + 1].split(",")  # next
        current_x = int(current_xy[0])
        current_y = int(current_xy[1])
        next_x = int(next_xy[0])
        next_y = int(next_xy[1])
        if current_x == next_x:
            if next_y < current_y:
                current_y, next_y = next_y, current_y
            for y in range(current_y, next_y + 1):
                cave[(current_x, y)] = "#"
        elif current_y == next_y:
            if next_x < current_x:
                current_x, next_x = next_x, current_x
            for x in range(current_x, next_x + 1):
                cave[(x, current_y)] = "#"
        else:
            print("This cannot happen")
            break


def print_cave(cave):
    for y in range(200):
        for x in range(600):
            cell = cave.get((x, y))
            if cell is None:
                print(".", end="")
            else:
                print(cell, end="")
        print()


print_cave(cave)
# %%

grain_x = 500
grain_y = 0
grain_count = 0

while True:

    if grain_y > 200:
        break

    if not cave.get((grain_x, grain_y + 1)):
        grain_y += 1
    elif not cave.get((grain_x - 1, grain_y + 1)):
        grain_x -= 1
        grain_y += 1
    elif not cave.get((grain_x + 1, grain_y + 1)):
        grain_x += 1
        grain_y += 1
    else:
        cave[(grain_x, grain_y)] = "o"
        grain_count += 1
        grain_x = 500
        grain_y = 0

print(grain_count)

# %%

# Build the map
cave = {}

for row in input_text:
    edges = row.split(" -> ")
    for i in range(len(edges) - 1):
        current_xy = edges[i].split(",")  # current
        next_xy = edges[i + 1].split(",")  # next
        current_x = int(current_xy[0])
        current_y = int(current_xy[1])
        next_x = int(next_xy[0])
        next_y = int(next_xy[1])
        if current_x == next_x:
            if next_y < current_y:
                current_y, next_y = next_y, current_y
            for y in range(current_y, next_y + 1):
                cave[(current_x, y)] = "#"
        elif current_y == next_y:
            if next_x < current_x:
                current_x, next_x = next_x, current_x
            for x in range(current_x, next_x + 1):
                cave[(x, current_y)] = "#"
        else:
            print("This cannot happen")
            break


def print_cave(cave):
    for y in range(200):
        for x in range(1200):
            cell = cave.get((x, y))
            if cell is None:
                print(".", end="")
            else:
                print(cell, end="")
        print()


print_cave(cave)
# %%

maxy = 0
for key in cave.keys():
    if key[1] > maxy:
        maxy = key[1]
maxy
for x in range(-1000, 1000):
    cave[(x, maxy + 2)] = "#"

print_cave(cave)

# %%

grain_x = 500
grain_y = 0
grain_count = 0

while True:

    if not cave.get((grain_x, grain_y + 1)):
        grain_y += 1
    elif not cave.get((grain_x - 1, grain_y + 1)):
        grain_x -= 1
        grain_y += 1
    elif not cave.get((grain_x + 1, grain_y + 1)):
        grain_x += 1
        grain_y += 1
    else:
        cave[(grain_x, grain_y)] = "o"
        grain_count += 1
        if grain_x == 500 and grain_y == 0:
            break
        grain_x = 500
        grain_y = 0

print(grain_count)

# %%
