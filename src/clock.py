import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def tick(self, fps):
        if not self.paused:
            self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time_get_ticks()
