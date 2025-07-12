"""Entry point for Fate of Rolls."""
from __future__ import annotations

import pygame
from pygame.locals import QUIT

from .player import Player
from .gacha import Gacha
from .battle import Battle, BattleResult
from .save_manager import load_player, save_player


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = load_player()
    gacha = Gacha()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((0, 0, 0))
        # Placeholder UI text
        font = pygame.font.Font(None, 36)
        text = font.render("Fate of Rolls - Placeholder", True, (255, 255, 255))
        screen.blit(text, (20, 20))
        pygame.display.flip()
        clock.tick(60)

    save_player(player)
    pygame.quit()


if __name__ == "__main__":
    main()
