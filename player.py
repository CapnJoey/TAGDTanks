import pygame as pg
from numpy import cos, sin, deg2rad

from bullet import Bullet
from controller import EnemyBullet

class Player:
    def __init__(self, game, controller, enemy, start_x: float=1.0, start_y: float=1.0, start_dir: int=0, tag: int=1) -> None:
        # Player state variables
        self.x = start_x
        self.y = start_y
        self.body_direction = start_dir
        self.gun_direction = start_dir
        self.tag = tag

        self.body_turn_speed = 360 / 2
        self.gun_turn_speed = 360 / 2
        self.move_speed = 1.5
        self.shoot_timer = 0.0
        self.shoot_cooldown_time = 1.0

        # Parent game
        self.game = game
        # Child controller
        self.controller = controller
        # Enemy
        self.enemy = enemy

        # Load image assets
        self.body_image = pg.image.load("./assets/tank.png").convert_alpha()
        self.body_image = pg.transform.scale(self.body_image, (32, 32))

        self.gun_image = pg.Surface((16, 8)).convert_alpha()
        self.gun_image.fill((0, 255, 0))

    def update(self):
        # Reset the controller state
        self.controller.body_turn_action = None
        self.controller.gun_turn_action = None
        self.controller.move_action = None
        self.controller.shoot_action = False
        self.controller.gun_ready = self.shoot_timer <= 0.0
        self.controller.enemy_bullets = []
        for bullet in self.game.bullets:
            if bullet.tag == self.tag: 
                continue
            dummy_bullet = EnemyBullet(bullet.x, bullet.y, bullet.direction)
            self.controller.enemy_bullets.append(dummy_bullet)

        # Update state variables
        self.controller.x = self.x
        self.controller.y = self.y
        self.controller.enemy_x = self.enemy.x
        self.controller.enemy_y = self.enemy.y
        self.controller.body_direction = self.body_direction
        self.controller.gun_direction = self.gun_direction
        self.controller.map = self.game.level.map

        # Call the user controller method
        self.controller.update()

        # Apply the user changes
        dt = self.game.dt

        # Body turning
        if self.controller.body_turn_action == 'clockwise':
            self.body_direction -= self.body_turn_speed * dt
        if self.controller.body_turn_action == 'counter_clockwise':
            self.body_direction += self.body_turn_speed * dt

        # Gun turning
        if self.controller.gun_turn_action == 'clockwise':
            self.gun_direction -= self.gun_turn_speed * dt
        if self.controller.gun_turn_action == 'counter_clockwise':
            self.gun_direction += self.gun_turn_speed * dt

        # Movement
        if self.controller.move_action == 'forward':
            self.x += self.move_speed * cos(deg2rad(self.body_direction)) * dt
            self.y += self.move_speed * sin(deg2rad(self.body_direction)) * dt
        if self.controller.move_action == 'backward':
            self.x -= self.move_speed * cos(deg2rad(self.body_direction)) * dt
            self.y -= self.move_speed * sin(deg2rad(self.body_direction)) * dt

        # Shoot
        self.shoot_timer -= dt
        if self.shoot_timer <= 0.0 and self.controller.shoot_action:
            x = self.x + cos(deg2rad(self.gun_direction)) * 0.3
            y = self.y + sin(deg2rad(self.gun_direction)) * 0.3
            bullet = Bullet(x, y, self.gun_direction, self.tag)
            self.game.bullets.append(bullet)
            self.shoot_timer = self.shoot_cooldown_time


    def render_to(self, surf: pg.Surface):
        layers = 5
        separation = 1
        center = (self.x * 32, (15 - self.y) * 32 + layers * separation)

        # Render body: rotate once, blit at stacked offsets
        rotated = pg.transform.rotate(self.body_image, self.body_direction)
        for stack_y in range(layers):
            rect = rotated.get_rect(center=(center[0], center[1] - stack_y * separation))
            surf.blit(rotated, rect)

        # Render gun on top of the stack
        rotated = pg.transform.rotate(self.gun_image, self.gun_direction)
        rect = rotated.get_rect(center=(center[0], center[1] - layers * separation))
        surf.blit(rotated, rect)