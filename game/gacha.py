from __future__ import annotations

import json
import random
from pathlib import Path
from typing import List

from .character import Character
from .constants import RARITY_RATES

CHARACTER_POOL = [
    {"name": "Warrior", "rarity": 3},
    {"name": "Mage", "rarity": 4},
    {"name": "Healer", "rarity": 2},
    {"name": "Rogue", "rarity": 3},
    {"name": "Paladin", "rarity": 5},
    {"name": "Archer", "rarity": 4},
]


class Gacha:
    def __init__(self) -> None:
        self.pool = CHARACTER_POOL

    def pull(self, count: int = 1) -> List[Character]:
        results = []
        for _ in range(count):
            rarity = self.choose_rarity()
            candidates = [c for c in self.pool if c["rarity"] == rarity]
            choice = random.choice(candidates)
            results.append(Character(name=choice["name"], rarity=choice["rarity"]))
        return results

    def choose_rarity(self) -> int:
        roll = random.random()
        cumulative = 0.0
        for rarity, rate in sorted(RARITY_RATES.items(), reverse=True):
            cumulative += rate
            if roll <= cumulative:
                return rarity
        return 1
