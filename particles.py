from math import cos, sin
import pygame as pg


class Particle:
    def __init__(self, x: float, y: float, size: float, color: tuple[int, int, int], speed: float, direction: float, lifetime: float, shape: str, shadow: bool=False):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.direction = direction
        self.lifetime = lifetime
        self.shape = shape
        self.shadow = shadow
        self.alive = True

    def update(self, dt: float):
        # Update the position of the particle
        self.x += self.speed * cos(self.direction) * dt
        self.y += self.speed * sin(self.direction) * dt
        
        # Check if the particle has expired
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.alive = False


class ParticleSystem:
    def __init__(self, game):
        self.game = game
        self.particles = []

    def update(self):
        # Update all particles
        for particle in self.particles:
            particle.update(self.game.dt)
        # Remove dead particles
        self.particles = [particle for particle in self.particles if particle.alive]

    def render(self, surface: pg.Surface):
        # Render the particles
        for particle in self.particles:
            # Render based on the shape
            x, y = particle.x * 32, 480 - particle.y * 32
            if particle.shape == 'circle':
                if particle.shadow:
                    pg.draw.circle(surface, (0, 0, 0, 255), (x + 2, y + 2), particle.size)

                pg.draw.circle(surface, particle.color, (x, y), particle.size)
            
            elif particle.shape == 'square':
                if particle.shadow:
                    pg.draw.rect(surface, (0, 0, 0, 255), (x + 2, y + 2, particle.size, particle.size), 1)

                pg.draw.rect(surface, particle.color, (x, y, particle.size, particle.size))

    def add_particle(self, x: float, y: float, size: float, color: tuple[int, int, int], speed: float, direction: float, lifetime: float, shape: str, shadow: bool=False):
        self.particles.append(Particle(x, y, size, color, speed, direction, lifetime, shape, shadow))