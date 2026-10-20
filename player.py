import pygame as pg
from numpy import cos, sin, deg2rad

class Player:
    def __init__(self, game, controller, enemy, start_x: float=1.0, start_y: float=1.0, start_dir: float=0.0) -> None:
        # Player state variables
        self.x = start_x
        self.y = start_y
        self.body_direction = start_dir
        self.gun_direction = start_dir

        self.body_turn_speed = 360 / 2
        self.gun_turn_speed = 360 / 2
        self.move_speed = 1.5

        # Parent game
        self.game = game
        # Child controller
        self.controller = controller
        # Enemy
        self.enemy = enemy

        # Load image assets
        self.body_image = pg.Surface((32, 32)).convert_alpha()
        self.gun_image = pg.Surface((32, 32)).convert_alpha()
        self.body_image.fill((255, 0, 0))
        self.gun_image.fill((0, 255, 0))

    def update(self):
        # Reset the controller state
        self.controller.body_turn_action = None
        self.controller.gun_turn_action = None
        self.controller.move_action = None
        self.controller.shoot_action = False

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
            self.body_direction += self.body_turn_speed * dt
        if self.controller.body_turn_action == 'counter_clockwise':
            self.body_direction -= self.body_turn_speed * dt

        # Gun turning
        if self.controller.gun_turn_action == 'clockwise':
            self.gun_direction += self.gun_turn_speed * dt
        if self.controller.gun_turn_action == 'counter_clockwise':
            self.gun_direction -= self.gun_turn_speed * dt

        # Movement
        if self.controller.move_action == 'forward':
            self.x += self.move_speed * cos(deg2rad(self.body_direction)) * dt
            self.y += self.move_speed * sin(deg2rad(self.body_direction)) * dt
        if self.controller.move_action == 'backward':
            self.x -= self.move_speed * cos(deg2rad(self.body_direction)) * dt
            self.y -= self.move_speed * sin(deg2rad(self.body_direction)) * dt


    def render_to(self, surf: pg.Surface):
        # Center of the tile in screen coordinates
        center = (self.x * 32, (15 - self.y) * 32)

        # Render body and gun at respective directions
        for image, angle in (
            (self.body_image, self.body_direction),
            (self.gun_image, self.gun_direction),
        ):
            rotated = pg.transform.rotate(image, angle)
            rect = rotated.get_rect(center=center)
            surf.blit(rotated, rect)