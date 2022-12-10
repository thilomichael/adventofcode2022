# %%
with open("input.txt", "r") as f:
    current_value = 0
    sum_values = []
    for row in f.readlines():
        r = row.strip()
        if r == "":
            sum_values.append(current_value)
            current_value = 0
        else:
            current_value += int(r)
    sum_values.sort(reverse=True)
    print(sum_values[0])


# %%
with open("input.txt", "r") as f:
    current_value = 0
    sum_values = []
    for row in f.readlines():
        r = row.strip()
        if r == "":
            sum_values.append(current_value)
            current_value = 0
        else:
            current_value += int(r)
    sum_values.sort(reverse=True)
    print(sum(sum_values[:3]))
# %%
