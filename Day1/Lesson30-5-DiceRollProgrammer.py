import random

# Dice ASCII art stored as lists of strings (one line per row)
dice_art = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}

dice = []
total = 0

num_of_dice = int(input("How many dice do you want to roll? "))

# Roll dice
for _ in range(num_of_dice):
    dice.append(random.randint(1, 6))

"""
# Print dice vertically
for die in dice:
    for line in dice_art[die]:
        print(line)
    print()  # Empty line between dice

"""
# Print dice horizontally
for line in range(len(dice_art[1])):
    for die in dice:
        print(dice_art[die][line], end="")
    print()


# Total
total = sum(dice)
print(f"Total: {total}")
