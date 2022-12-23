# %% ==

with open("input.txt", "r") as f:
    input_text = f.read().split("\n")
input_text

# input_text = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""
# input_text = input_text.split("\n")
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

input_packets = [eval(x) for x in input_text]
