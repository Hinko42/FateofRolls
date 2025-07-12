from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List

from .constants import roll_dice

@dataclass
class Ability:
    """Represents an ability that a character can use."""
    name: str
    power: int
    dice: int = 20  # default d20 roll for success
    effect: Callable[[Character, Character], None] | None = None

    def use(self, user: "Character", target: "Character") -> bool:
        """Attempt to use the ability, returning True on success."""
        if roll_dice(self.dice) > 5:
            if self.effect:
                self.effect(user, target)
            return True
        return False

@dataclass
class Character:
    name: str
    rarity: int
    level: int = 1
    max_hp: int = 100
    attack: int = 10
    defense: int = 5
    abilities: List[Ability] = field(default_factory=list)

    hp: int = field(init=False)

    def __post_init__(self) -> None:
        self.hp = self.max_hp

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def basic_attack(self, target: "Character") -> None:
        dmg = max(1, self.attack - target.defense)
        target.take_damage(dmg)

    def use_ability(self, ability: Ability, target: "Character") -> bool:
        return ability.use(self, target)
