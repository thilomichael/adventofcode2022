# %% ===

with open("input.txt", "r") as f:
    input_text = f.read().strip().split("\n")

input_text
# %%

import math

BIG_MODULO = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19


class Monkey:
    def __init__(self, monkey_id, items, operation, divider, true_monkey, false_monkey):
        self.monkey_id = monkey_id
        self.current_items = items
        self.operation = operation
        self.divider = divider
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.inspect_counter = 0

    def throw_item(self, divide_by_three=True):
        # print("Current monkey:", self)

        # Get first item out of list
        item = self.current_items.pop(0)
        # print("item", item)

        # Increase inspect counter
        self.inspect_counter += 1

        # Increase concern for that item with operation
        operation = self.operation.replace("old", str(item))
        item = eval(operation)
        # print("operation", operation)
        # print("increased item", item)

        # Decrease concern by dividing by 3 and rounding down
        if divide_by_three:
            item = int(math.floor(item / 3))
            # print("decreased item", item)

        # Perform the test and determin which monkey to throw to
        receiving_monkey = None
        # print("tr fa monkey", self.true_monkey, self.false_monkey)
        # print("divider", self.divider)
        if item % self.divider == 0:
            receiving_monkey = self.true_monkey
        else:
            receiving_monkey = self.false_monkey
        # print("receiving monkey", receiving_monkey)

        if not divide_by_three:
            item = item % BIG_MODULO
        # Return item and monkey to throw to
        return item, receiving_monkey

    def receive_item(self, item):
        self.current_items.append(item)

    def has_items(self):
        return len(self.current_items) != 0

    def __repr__(self):
        return f"Monkey {self.monkey_id} ({self.current_items})"


# Parse monkeys
def init_monkeys():
    monkeys = []
    for i in range(0, len(input_text), 7):
        # Monkey ID
        monkey_id = int(input_text[i].split(" ")[-1].split(":")[0])

        # Starting items
        starting_items = input_text[i + 1].replace("  Starting items: ", "")
        starting_items = [int(x) for x in starting_items.split(",")]

        # Opartion
        operation = input_text[i + 2].replace("  Operation: new = ", "")

        # Divider
        divider = int(input_text[i + 3].replace("  Test: divisible by ", ""))

        # Next monkeys
        true_monkey = int(input_text[i + 4].split(" ")[-1])
        false_monkey = int(input_text[i + 5].split(" ")[-1])

        # Create monkeys and store them in array
        m = Monkey(
            monkey_id, starting_items, operation, divider, true_monkey, false_monkey
        )
        monkeys.append(m)
    return monkeys


monkeys = init_monkeys()

# %% ==

for round in range(20):
    for monkey in monkeys:
        while monkey.has_items():
            item, receiving_monkey = monkey.throw_item(divide_by_three=True)
            monkeys[receiving_monkey].receive_item(item)

# %%

for monkey in monkeys:
    print(monkey.monkey_id, monkey.inspect_counter)

# %%

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspect_counter)
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
# %% PART TWO

monkeys = init_monkeys()

for round in range(10_000):
    for monkey in monkeys:
        while monkey.has_items():
            item, receiving_monkey = monkey.throw_item(divide_by_three=False)
            monkeys[receiving_monkey].receive_item(item)

for monkey in monkeys:
    print(monkey.monkey_id, monkey.inspect_counter)

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspect_counter)
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
# %%
