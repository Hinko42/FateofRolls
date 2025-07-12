import random

# Dice rolling utilities

def roll_dice(sides: int = 6) -> int:
    """Roll a die with the given number of sides."""
    return random.randint(1, sides)

# Rarity probabilities for gacha pulls
RARITY_RATES = {
    5: 0.05,
    4: 0.20,
    3: 0.35,
    2: 0.25,
    1: 0.15,
}
