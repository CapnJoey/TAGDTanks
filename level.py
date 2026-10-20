import pygame as pg
import numpy as np

class Level:
    def __init__(self) -> None:
        self.surface = pg.Surface((32 * 20, 32 * 15)).convert()

        # Map
        self.fill_map()

        # Load enviornment images
        self.bg_image = pg.image.load("./assets/bg.png").convert()
        self.rock_image = [pg.image.load(f"./assets/rock{i+1}.png") for i in range(6)]

    def fill_map(self) -> None:
        # Make empty map
        self.map = np.zeros((20, 15))  

        # Always add border
        for x in range(20):
            self.map[x][0] = 1
            self.map[x][-1] = 1
        for y in range(15):
            self.map[0][y] = 1
            self.map[-1][y] = 1

        # Add real map

    def render(self) -> None:
        self.surface.fill((255, 255, 255, 1))

        # Add bg
        self.surface.blit(self.bg_image, (0, 0))

        for x in range(20):
            for y in range(15):
                if not self.map[x][y]: continue
                self.surface.blit(self.rock_image[0], (x * 32, y * 32))

    def blit_to(self, surf: pg.Surface, location: tuple=None) -> None:
        location = location or (0, 0)
        surf.blit(self.surface, location)