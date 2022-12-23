# %% ==

with open("input.txt", "r") as f:
    input_text = f.read().split("\n")
input_text
# %%


def in_order(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            order = in_order(l, r)
            if order != None:
                return order
        if len(right) < len(left):
            return False
        elif len(left) < len(right):
            return True
        else:
            return None
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    else:
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return in_order(left, right)


sum = 0
for index, i in enumerate(range(0, len(input_text), 3)):
    left = eval(input_text[i])
    right = eval(input_text[i + 1])

    if in_order(left, right):
        sum += index + 1

print(sum)

# %%

input_packets = [eval(x) for x in input_text if x.strip() != ""]

# Append divider packets
input_packets.append([[2]])
input_packets.append([[6]])


def compare(left, right):
    order = in_order(left, right)
    if order == True:
        return -1
    elif order == False:
        return 1
    else:
        return 0


from functools import cmp_to_key

sorted_packets = sorted(input_packets, key=cmp_to_key(compare))

index_2 = sorted_packets.index([[2]]) + 1
index_6 = sorted_packets.index([[6]]) + 1
print(index_2 * index_6)
# %%
