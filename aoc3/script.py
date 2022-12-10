# %% ===

with open("input.txt", "r") as f:
    priority_sum = 0
    for row in f.readlines():
        r = row.strip()
        left = r[: int(len(r) / 2)]
        right = r[int(len(r) / 2) :]
        left = set(left)
        right = set(right)
        element = left.intersection(right)
        element = element.pop()

        if element == element.lower():
            priority = ord(element) - 96
        else:
            priority = ord(element) - 38

        priority_sum += priority

    print(priority_sum)


# %% ===

with open("input.txt", "r") as f:
    priority_sum = 0
    current_set = {}
    for i, row in enumerate(f.readlines()):
        r = row.strip()
        rset = set(r)

        if i % 3 == 0:
            current_set = rset
        elif i % 3 == 1:
            current_set = current_set.intersection(rset)
        elif i % 3 == 2:
            current_set = current_set.intersection(rset)
            element = current_set.pop()

            if element == element.lower():
                priority = ord(element) - 96
            else:
                priority = ord(element) - 38

            priority_sum += priority

    print(priority_sum)

# %%
