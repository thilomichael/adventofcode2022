# %% ===

with open("input.txt", "r") as f:
    line = f.readline().strip()
    print(line)


def detect_message(pattern_length):
    current_characters = []
    for i, character in enumerate(line):
        current_characters.append(character)

        if len(current_characters) < pattern_length:
            continue
        if len(current_characters) > pattern_length:
            current_characters.pop(0)

        if len(set(current_characters)) == len(current_characters):
            print(i + 1)
            break


detect_message(4)

# %% ===

detect_message(14)
# %%
