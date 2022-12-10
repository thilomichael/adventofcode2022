# %% ===

with open("input.txt", "r") as f:
    input_text = f.read()

commands = input_text.strip().split("\n")
len(commands)

# %%

cycle = 0
X_register = 1
signal_strength = 0

ci = 0

current_number = 0
addx_flag = 0

offset = 20
period = 40

while True:
    # increae cycle
    cycle += 1

    # execute command
    if addx_flag == 0:
        if ci == len(commands):  # No more commands
            break
        command = commands[ci]
        ci += 1
        if command == "noop":
            pass
        elif command[:4] == "addx":
            current_number = int(command[5:])
            addx_flag = 2

    # check signal strength
    if cycle % period == offset:
        signal_strength += cycle * X_register

    # update X_register
    if addx_flag == 2:
        addx_flag = 1
    elif addx_flag == 1:
        addx_flag = 0
        X_register += current_number

print(signal_strength)
# %%

import time

cycle = 0
X_register = 1

ci = 0

current_number = 0
addx_flag = 0

offset = 1
period = 40

while True:
    # increae cycle
    cycle += 1

    # execute command
    if addx_flag == 0:
        if ci == len(commands):  # No more commands
            break
        command = commands[ci]
        ci += 1
        if command == "noop":
            pass
        elif command[:4] == "addx":
            current_number = int(command[5:])
            addx_flag = 2

    position = (cycle - 1) % period
    if abs(position - X_register) <= 1:
        print("█", end="", flush=True)
    else:
        print(" ", end="", flush=True)

    if cycle % period == offset - 1:
        print("")

    print("_", end="", flush=True)

    time.sleep(0.02)

    print("\b", end="", flush=True)

    # update X_register
    if addx_flag == 2:
        addx_flag = 1
    elif addx_flag == 1:
        addx_flag = 0
        X_register += current_number
# %%
