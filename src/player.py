import os
import pygame

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, cell_size, x=0, y=0):
        super().__init__()

        self._cell_size = cell_size
        self.time_since_update = 0
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = (x*self._cell_size)
        self.rect.y = (y*self._cell_size)

    def update(self, time):
        pass