import pygame as pg
from numpy import sin, cos, sqrt, pi, deg2rad
from math import floor, ceil

class Bullet:
    def __init__(self, start_x: float=10, start_y: float=7, direction: int=0, tag: int=0, image: pg.Surface|None=None) -> None:
        self.x = start_x
        self.y = start_y
        self.direction = direction
        self.tag = tag

        self.bounce_count = 0
        self.max_bounces = 1
        self.speed = 5
        self.dead = False

        if image:
            self.bullet_image = image
        else:
            self.bullet_image = pg.Surface((6, 6)).convert_alpha()
            self.bullet_image.fill((0, 0, 255))


    @staticmethod
    def _is_wall(map, x: float, y: float) -> bool:
        gx, gy = int(floor(x)), int(floor(y))
        if gx < 0 or gy < 0 or gx >= len(map) or gy >= len(map[0]):
            return True  # treat out of bounds as a wall
        return bool(map[gx][gy])

    def _bounce(self) -> bool:
        """Register a bounce. Returns False if the bullet should die instead."""
        if self.bounce_count >= self.max_bounces:
            self.dead = True
            return False
        self.bounce_count += 1
        return True


    def update(self, players, map, dt):
        dx = cos(deg2rad(self.direction)) * self.speed * dt
        dy = sin(deg2rad(self.direction)) * self.speed * dt

        # Move on X, check for wall
        if self._is_wall(map, self.x + dx, self.y):
            if not self._bounce():
                return
            self.direction = (180 - self.direction) % 360  # flip x component
        else:
            self.x += dx

        # Move on Y, check for wall
        if self._is_wall(map, self.x, self.y + dy):
            if not self._bounce():
                return
            self.direction = (-self.direction) % 360  # flip y component
        else:
            self.y += dy

        # Player collision
        for player in players:
            if player.tag == self.tag:
                continue
            if sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2) <= 0.5:
                player.alive = False
                self.dead = True

    def render_to(self, surf: pg.Surface):
        # Center of the tile in screen coordinates
        center = (self.x * 32, (15 - self.y) * 32)

        # Render body and gun at respective directions
        rotated = pg.transform.rotate(self.bullet_image, self.direction)
        rect = rotated.get_rect(center=center)
        surf.blit(rotated, rect)