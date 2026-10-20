import pygame as pg


class Player:
    def __init__(self, controller, start_x: float=1.0, start_y: float=1.0, start_dir: float=0.0) -> None:
        # Player state variables
        self.x = start_x
        self.y = start_y
        self.body_direction = start_dir
        self.gun_direction = start_dir

        # Child controller
        self.controller = controller

        # Load image assets
        self.body_image = pg.Surface((32, 32)).convert_alpha()
        self.gun_image = pg.Surface((32, 32)).convert_alpha()
        self.body_image.fill((255, 0, 0))
        self.gun_image.fill((0, 255, 0))

    def update(self):
        self.controller.tur
        self.controller.update()

    def render_to(self, surf: pg.Surface):
        # Center of the tile in screen coordinates
        center = (self.x * 32, (15 - self.y) * 32)

        for image, angle in (
            (self.body_image, self.body_direction),
            (self.gun_image, self.gun_direction),
        ):
            rotated = pg.transform.rotate(image, angle)
            rect = rotated.get_rect(center=center)
            surf.blit(rotated, rect)