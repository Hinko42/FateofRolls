from __future__ import annotations

import random
from enum import Enum, auto
from typing import List

from .character import Character, Ability
from .ai import EnemyAI
from .constants import roll_dice


class BattleResult(Enum):
    PLAYER_WIN = auto()
    ENEMY_WIN = auto()
    ONGOING = auto()


class Battle:
    """Simple 3v3 battle manager."""

    def __init__(self, player_team: List[Character], enemy_team: List[Character], ai: EnemyAI | None = None) -> None:
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.ai = ai or EnemyAI()
        self.turn_order = self.player_team + self.enemy_team
        random.shuffle(self.turn_order)
        self.turn_index = 0

    def get_current_actor(self) -> Character:
        return self.turn_order[self.turn_index]

    def next_turn(self) -> None:
        self.turn_index = (self.turn_index + 1) % len(self.turn_order)

    def perform_turn(self) -> BattleResult:
        actor = self.get_current_actor()
        if actor in self.enemy_team:
            target = self.ai.choose_target(self.player_team)
            ability = self.ai.choose_ability(actor)
            actor.use_ability(ability, target)
        else:
            # Placeholder: player always attacks first enemy
            target = next((e for e in self.enemy_team if e.is_alive()), None)
            if target:
                actor.basic_attack(target)
        self.cleanup()
        self.next_turn()
        return self.check_result()

    def cleanup(self) -> None:
        self.player_team = [c for c in self.player_team if c.is_alive()]
        self.enemy_team = [c for c in self.enemy_team if c.is_alive()]
        self.turn_order = [c for c in self.turn_order if c.is_alive()]

    def check_result(self) -> BattleResult:
        if not self.player_team:
            return BattleResult.ENEMY_WIN
        if not self.enemy_team:
            return BattleResult.PLAYER_WIN
        return BattleResult.ONGOING
