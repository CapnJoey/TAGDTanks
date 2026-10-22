import pygame as pg
import numpy as np
from numpy import cos, sin, deg2rad

from bullet import Bullet
from controller import EnemyBullet

def collide(map: np.ndarray, x: float, y: float) -> tuple[float, float]:
    """
    Returns new position of Player after collision with map walls
    Doesn't change position if there is no collision
    """
    r = 0.5
    # get 2x2 grid containing player
    gx = int(np.floor(x - r))
    gy = int(np.floor(y - r))

    for i in (gx, gx + 1):
        for j in (gy, gy + 1):
            # check to see if the player is colliding with any of the walls
            if i < 0 or j < 0 or i >= map.shape[0] or j >= map.shape[1]:
                continue
            if not map[i][j]:
                continue

            # resolve with the minimal translation vector   
            overlap_x = min(x + r, i + 1) - max(x - r, i)
            overlap_y = min(y + r, j + 1) - max(y - r, j)
            if overlap_x <= 0 or overlap_y <= 0:
                continue

            if overlap_x < overlap_y: 
                x += overlap_x if x > i + 0.5 else -overlap_x
            else: 
                y += overlap_y if y > j + 0.5 else -overlap_y

    return x, y

class Player:
    def __init__(self, game, user, enemy, start_x: float=1.0, start_y: float=1.0, start_dir: int=0, tag: int=1) -> None:
        # Player state variables
        self.x = start_x
        self.y = start_y
        self.body_direction = start_dir
        self.gun_direction = start_dir
        self.tag = tag
        self.alive = True

        self.body_turn_speed = 360 / 2
        self.gun_turn_speed = 360 / 2
        self.move_speed = 1.5
        self.shoot_timer = 0.0
        self.shoot_cooldown_time = 3.0

        # User
        self.user = user
        # User controller
        self.controller = user.controller
        # Parent game
        self.game = game
        # Enemy
        self.enemy = enemy

        # Load image assets
        self.body_images = user.tank_images
        self.gun_images = user.gun_images
        self.bullet_image = user.bullet_image
        self.name_font = pg.font.Font("./assets/upheavtt.ttf", 16)

        # Set up animation variables
        self.body_animation_frame = 0
        self.gun_animation_frame = 0
        self.animation_time = 0.1
        self.frame_timer = 0.0
        self.moving = False
        self.shooting = 0

    def update(self):

        # Get delta time
        dt = self.game.dt
        
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
            
        dt = self.game.dt

        # Update state variables
        self.controller.x = self.x
        self.controller.y = self.y
        self.controller.enemy_x = self.enemy.x
        self.controller.enemy_y = self.enemy.y
        self.controller.body_direction = self.body_direction
        self.controller.gun_direction = self.gun_direction
        self.controller.map = self.game.level.map
        self.controller.dt = dt

        # Call the user controller method
        if self.alive:
            if self.game.game_over:
                self.controller.body_turn_action = 'clockwise'
                self.controller.gun_turn_action  = 'counter_clockwise'
            else:
                self.controller.update()

        # Update animations
        self.frame_timer += dt
        if self.frame_timer > self.animation_time:
            self.body_animation_frame = (self.body_animation_frame + 1) % 3
            self.gun_animation_frame  = (self.body_animation_frame + 1) % 3
            self.frame_timer = 0.0
            self.shooting -= 1

        # Apply the user changes
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

        self.x, self.y = collide(self.game.level.map, self.x, self.y)

        self.moving = (
            self.controller.move_action == 'forward' or
            self.controller.move_action == 'backward' or
            self.controller.body_turn_action == 'clockwise' or
            self.controller.body_turn_action == 'counter_clockwise'
        )

        # Shoot
        self.shoot_timer -= dt
        if self.shoot_timer <= 0.0 and self.controller.shoot_action:
            x = self.x + cos(deg2rad(self.gun_direction)) * 0.3
            y = self.y + sin(deg2rad(self.gun_direction)) * 0.3
            bullet = Bullet(self.game, x, y, self.gun_direction, self.tag, self.bullet_image)
            self.game.bullets.append(bullet)
            self.shoot_timer = self.shoot_cooldown_time
            self.game.shake_timer = 0.15
            self.shooting = 3
            self.gun_animation_frame = 0
            self.frame_timer = 0


    def render_to(self, surf: pg.Surface):
        layers = 5
        separation = 1
        center = (self.x * 32, (15 - self.y) * 32 + layers * separation)

        # Render body: rotate once, blit at stacked offsets
        body_image = self.body_images[self.body_animation_frame] if self.moving else self.body_images[-1]
        rotated = pg.transform.rotate(body_image, self.body_direction)
        for stack_y in range(layers):
            rect = rotated.get_rect(center=(center[0], center[1] - stack_y * separation))
            surf.blit(rotated, rect)

        # Render gun on top of the stack
        gun_image = self.gun_images[self.gun_animation_frame] if self.shooting > 0 else self.gun_images[-1]
        rotated = pg.transform.rotate(gun_image, self.gun_direction)
        rect = rotated.get_rect(center=(center[0], center[1] - layers * separation))
        surf.blit(rotated, rect)

        # Render the name
        font = self.name_font
        text = font.render(self.user.name, True, (255, 255, 255))
        font.outline = 1
        outline = font.render(self.user.name, True, (0, 0, 0))
        font.outline = 0
        name_center = (center[0], center[1] - layers * separation - 20)
        surf.blit(outline, outline.get_rect(center=name_center))
        surf.blit(text, text.get_rect(center=name_center))