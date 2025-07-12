import json
from pathlib import Path

from .player import Player
from .character import Character

SAVE_FILE = Path("save.json")


def save_player(player: Player) -> None:
    data = {
        "name": player.name,
        "tickets": player.tickets,
        "gold": player.gold,
        "campaign_stage": player.campaign_stage,
        "roster": [
            {
                "name": c.name,
                "rarity": c.rarity,
                "level": c.level,
                "max_hp": c.max_hp,
                "attack": c.attack,
                "defense": c.defense,
            }
            for c in player.roster
        ],
    }
    SAVE_FILE.write_text(json.dumps(data, indent=2))


def load_player() -> Player:
    if not SAVE_FILE.exists():
        return Player(name="Player")
    data = json.loads(SAVE_FILE.read_text())
    player = Player(name=data["name"], tickets=data["tickets"], gold=data["gold"], campaign_stage=data["campaign_stage"])
    for cdata in data["roster"]:
        char = Character(
            name=cdata["name"],
            rarity=cdata["rarity"],
            level=cdata["level"],
            max_hp=cdata["max_hp"],
            attack=cdata["attack"],
            defense=cdata["defense"],
        )
        player.roster.append(char)
    return player
