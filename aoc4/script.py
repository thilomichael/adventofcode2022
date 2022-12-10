# %% ===

with open("input.txt", "r") as f:
    counter = 0
    for row in f.readlines():
        r = row.strip().split(",")
        elve1 = r[0].split("-")
        elve2 = r[1].split("-")
        print(elve1, elve2)
        elve1_set = set(range(int(elve1[0]), int(elve1[1]) + 1))
        elve2_set = set(range(int(elve2[0]), int(elve2[1]) + 1))
        if elve1_set.issubset(elve2_set) or elve2_set.issubset(elve1_set):
            counter += 1
    print(counter)


# %% ===

with open("input.txt", "r") as f:
    counter = 0
    for row in f.readlines():
        r = row.strip().split(",")
        elve1 = r[0].split("-")
        elve2 = r[1].split("-")
        print(elve1, elve2)
        elve1_set = set(range(int(elve1[0]), int(elve1[1]) + 1))
        elve2_set = set(range(int(elve2[0]), int(elve2[1]) + 1))
        if len(elve1_set.intersection(elve2_set)) != 0:
            counter += 1
    print(counter)

# %%
