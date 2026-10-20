import pygame as pg

class Level:
    def __init__(self) -> None:
        self.surface = pg.Surface((32 *20, 32 * 15)).convert()

        # Load enviornment images
        self.bg_image = pg.image.load("./assets/bg.png").convert()

    def render(self) -> None:
        self.surface.fill((255, 0, 0, 1))
        self.surface.blit(self.bg_image, (0, 0))

    def blit_to(self, surf: pg.Surface, location: tuple=None) -> None:
        location = location or (0, 0)
        surf.blit(self.surface, location)