from dataclasses import dataclass, field
from typing import List

from .character import Character

@dataclass
class Player:
    """Represents a player's data and inventory."""
    name: str
    roster: List[Character] = field(default_factory=list)
    tickets: int = 0
    gold: int = 0
    campaign_stage: int = 0

    def add_character(self, character: Character) -> None:
        self.roster.append(character)

    def get_team(self, size: int = 3) -> List[Character]:
        """Return a subset of characters to form a team."""
        return self.roster[:size]
