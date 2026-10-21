import pygame as pg
import random
from maps import *


class Level:
    def __init__(self) -> None:
        self.surface = pg.Surface((32 * 20, 32 * 15)).convert()

        # Map
        self.fill_map()

        # Load enviornment images
        self.bg_image = pg.image.load("./assets/bgwalled.png").convert()
        self.rock_image = [pg.image.load(f"./assets/rock{i+1}.png") for i in range(6)]

    def fill_map(self) -> None:
        # Make empty map
        self.map = empty_map()

        # Add real map
        funcs = [plus_map, bars_map, rect_map]
        self.map = random.choice(funcs)(self.map)

    def render(self) -> None:
        self.surface.fill((255, 255, 255, 1))

        # Add bg
        self.surface.blit(self.bg_image, (0, 0))

        for x in range(20):
            for y in range(15):
                if not self.map[x][14 - y] == 1: continue
                self.surface.blit(self.rock_image[random.randrange(0, 6)], (x * 32, (14 - y) * 32))

    def blit_to(self, surf: pg.Surface, location: tuple=None) -> None:
        location = location or (0, 0)
        surf.blit(self.surface, location)