import pygame as pg
from numpy import sin, cos, sqrt, pi, deg2rad
from math import floor, ceil
import random

class Bullet:
    def __init__(self, game, start_x: float=10, start_y: float=7, direction: int=0, tag: int=0, image: pg.Surface|None=None) -> None:
        self.game = game
        self.x = start_x
        self.y = start_y
        self.direction = direction
        self.tag = tag

        self.bounce_count = 0
        self.max_bounces = 1
        self.speed = 5
        self.dead = False

        self.particle_system = game.particle_system
        self.particle_timer = 0.0
        self.particle_interval = 0.1

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
            self._add_impact_particles()
            self.game.shake_timer = 0.5
            return False
        self.bounce_count += 1
        return True

    def _add_trail_particles(self):
        direction = -1 * self.direction + random.randint(-10, 10)
        self.particle_system.add_particle(self.x, self.y, 3, (255, 255, 255), 1, direction, 1, 'circle', True)

    def _add_impact_particles(self):
        colors = [(255, 200, 100), (255, 150, 50), (255, 100, 0), (255, 255, 255)]
        for i in range(20):
            direction = random.randint(0, 360)
            size = random.uniform(2, 6)
            color = colors[random.randint(0, 3)]
            speed = random.uniform(2, 4)
            lifetime = random.uniform(0.2, 0.5)
            self.particle_system.add_particle(self.x, self.y, size, color, speed, direction, lifetime, 'circle', True)

    def update(self, players, map, dt):
        dx = cos(deg2rad(self.direction)) * self.speed * dt
        dy = sin(deg2rad(self.direction)) * self.speed * dt

        if self.game.game_over:
            self.dead = True
            return
            
        # Update particles
        self.particle_timer += dt
        if self.particle_timer >= self.particle_interval:
            self.particle_timer = 0.0
            self._add_trail_particles()

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
                self.game.game_over = True
                self._add_impact_particles()
                self.game.shake_timer = 0.5

    def render_to(self, surf: pg.Surface):
        # Center of the tile in screen coordinates
        center = (self.x * 32, (15 - self.y) * 32)

        # Render body and gun at respective directions
        rotated = pg.transform.rotate(self.bullet_image, self.direction)
        rect = rotated.get_rect(center=center)
        surf.blit(rotated, rect)