from __future__ import annotations

import random
from typing import List

from .character import Character, Ability


class EnemyAI:
    """Very simple AI for choosing actions."""

    def choose_target(self, enemies: List[Character]) -> Character:
        alive = [e for e in enemies if e.is_alive()]
        return random.choice(alive)

    def choose_ability(self, enemy: Character) -> Ability:
        if enemy.abilities:
            return random.choice(enemy.abilities)
        # fall back to basic attack wrapped as ability
        return Ability(name="Attack", power=enemy.attack, dice=6,
                       effect=lambda u, t: t.take_damage(max(1, u.attack - t.defense)))
