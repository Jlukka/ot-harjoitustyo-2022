import pygame

class Game:
    def __init__(self, maze, player, renderer, event_queue, clock, cell_size):
        self._maze = maze
        self._player = player
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            print(event)
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()