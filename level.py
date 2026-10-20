import pygame as pg
import numpy as np
import random

# map generation
def line_x(map: np.ndarray, x1: int, x2: int, y: int) -> np.ndarray:
    for x in range(x1, x2):
        map[x, y] = 1
    return map

def line_y(map: np.ndarray, y1: int, y2: int, x: int) -> np.ndarray:
    for y in range(y1, y2):
        map[x, y] = 1
    return map

def plus_map(map: np.ndarray) -> np.ndarray:
    map = line_x(map, 4, 16, 7)
    map = line_y(map, 3, 12, 9)
    map = line_y(map, 3, 12, 10)
    return map

def bars_map(map: np.ndarray) -> np.ndarray:
    map = line_y(map, 3, 12, 5)
    map = line_y(map, 3, 12, 15)
    return map

def rect_map(map: np.ndarray) -> np.ndarray:
    for y in range(4, 11):
        line_x(map, 4, 16, y)
    return map

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
        funcs = [plus_map, bars_map, rect_map]
        self.map = random.choice(funcs)(self.map)

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