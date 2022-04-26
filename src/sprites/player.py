import os
import pygame

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, grid, x=0, y=0):
        super().__init__()
        self.grid = grid

        self.last_update = 0
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png")
        )
        self.speed = 4
        self.current = (x,y)
        self.distance = 0
        self.direction = "r"
        self.next_direction = "r"
        self.next = self._find_next

        self.rect = self.image.get_rect()


    def _find_next(self, current):
        directions = {"l" : (-1, 0),
                      "u" : (0, 1),
                      "r" : (1, 0),
                      "d" : (0, -1)}
        current_x = self.current[0]
        current_y = self.current[1]
        new_x = current_x + directions[self.direction][0]
        new_y = current_y + directions[self.direction][1]
        if new_x < 0 or new_x > len(self.grid[0])-1:
            return current
        if new_y < 0 or new_y > len(self.grid)-1:
            return current
        
        return (new_x, new_y)


    def update(self, time, cell_size):
        timedelta = time - self.last_update
            




        self.rect.x = (x*self._cell_size)
        self.rect.y = (y*self._cell_size)

