import pygame
from sprites.floor import Floor
from sprites.gate import Gate
from sprites.wall import Wall


class Renderer:
    def __init__(self, display, maze, sprites, cell_size):
        self._display = display
        self._maze = maze
        self._sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.gates = pygame.sprite.Group()
        self._cell_size = cell_size
        self.__initialize_maze_sprites()

    def __initialize_maze_sprites(self):
        height = len(self._maze)
        width = len(self._maze[0])

        for y in range(height):
            for x in range(width):
                cell = self._maze[y][x]

                if cell == "0":
                    self.floors.add(Floor(x*self._cell_size, y*self._cell_size))
                elif cell == "1":
                    self.walls.add(Wall(x*self._cell_size, y*self._cell_size))
                elif cell == "2":
                    self.gates.add(Gate(x*self._cell_size, y*self._cell_size))


        self._sprites.add(
            self.walls,
            self.floors,
            self.gates
        )

