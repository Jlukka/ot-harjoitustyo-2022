from multiprocessing import Event
import pygame
from mazes.default import Default
from sprites.player import Player
from game import Game
from eventqueue import EventQueue
from renderer import Renderer
from clock import Clock

CELL_SIZE = 16

grid = Default.grid

player = Player(grid)

def main():
    height = len(grid)
    width = len(grid[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    event_queue = EventQueue()
    renderer = Renderer(display, grid, player, CELL_SIZE)
    clock = Clock()
    game = Game(Default, player, renderer, event_queue, clock, CELL_SIZE)

    pygame.init()
    game.start()


if __name__ == "__main__":
    main()