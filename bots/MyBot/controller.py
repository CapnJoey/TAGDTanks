import numpy as np
import pygame as pg
import random
from game_code.cheat_prevention import *


class EnemyBullet:
    def __init__(self, x: float, y: float, direction: int) -> None:
        """
        Represents an enemy bullet.
        
        Args:
            x: the x position of the bullet (in grid units)
            y: the y position of the bullet (in grid units)
            direction: the direction of the bullet (in degrees)
        """
        self.x         : float = x
        self.y         : float = y
        self.direction : int   = direction


class Controller:
    def __init__(self) -> None:
        # Initialize state variables
        self.x              : float             = 0
        self.y              : float             = 0
        self.enemy_x        : float             = 0
        self.enemy_y        : float             = 0
        self.body_direction : int               = 0
        self.gun_direction  : int               = 0
        self.gun_ready      : bool              = False
        self.enemy_bullets  : list[EnemyBullet] = []
        self.map            : np.ndarray        = np.zeros((20, 15))
        self.dt             : float             = 0

        # Initialize action variables
        self.body_turn_action = None
        self.gun_turn_action  = None
        self.move_action      = None
        self.shoot_action     = False

        # DEFINE CUSTOM STATE VARIABLES (optional)



        # END DEFINE CUSTOM STATE VARIABLES (optional)

    def update(self):
        """
        Write your bot code here. This will be called every frame to determine the next action.

        Actions you can take (all methods have no arguments):
        - self.turn_body_clockwise()
        - self.turn_body_counter_clockwise()
        - self.turn_gun_clockwise()
        - self.turn_gun_counter_clockwise()
        - self.move_forward()
        - self.move_backward()
        - self.shoot()

        Values you can use:
        - self.x: the x position of the tank (in grid units)
        - self.y: the y position of the tank (in grid units)
        - self.enemy_x: the x position of the enemy tank (in grid units)
        - self.enemy_y: the y position of the enemy tank (in grid units)
        - self.body_direction: the current direction of the body (in degrees)
        - self.gun_direction: the current direction of the gun (in degrees)
        - self.gun_ready: whether the gun is ready to shoot (True or False)
        - self.enemy_bullets: a list of enemy bullets (see EnemyBullet class for more information)
        - self.map: the current map (a 20x15 numpy array, where map[x][y] == True if there is a wall, False otherwise)
        - self.dt: the time since the last frame (in seconds)

        Notes:
            - Tank and body directions are independent. Turning the body will not affect the gun direction.

            - You cannot set your own properties, or the properties of the enemy or bullets. You can only set the action variables.
                For example:
                    self.x = 10  # WILL NOT WORK
                Use:
                    self.move_forward()  # Instead
        
            - If your code throws an error, it will be caught and your tank will be killed.
        """

        # START YOUR CODE HERE

        

        # END YOUR CODE HERE


    def turn_body_clockwise(self): 
        self.body_turn_action = "clockwise"

    def turn_body_counter_clockwise(self):
        self.body_turn_action = "counter_clockwise"
    
    def stop_turn_body(self):
        self.body_turn_action = None

    def turn_gun_clockwise(self):
        self.gun_turn_action = "clockwise"

    def turn_gun_counter_clockwise(self):
        self.gun_turn_action = "counter_clockwise"

    def stop_turn_gun(self):
        self.gun_turn_action = None

    def move_forward(self):
        self.move_action = "forward"

    def move_backward(self):
        self.move_action = "backward"

    def stop_move(self):
        self.move_action = None

    def shoot(self):
        self.shoot_action = True
        
    # ------------------------------------------------------------  
    # Helpful function Alert :O vvvvvv
    # ------------------------------------------------------------  
        
    def raycast(self) -> tuple[float, float] | None:
        """
        Shoot a ray from the tank's barrel and retrieve the hit position. 

        Returns:
            tuple[float, float]: The coordinate of the raycast hit.
            None: If no hit.
        """
        # walk the ray tile by tile
        # and anything outside the map counts as a wall
        dx = np.cos(np.deg2rad(self.gun_direction))
        dy = np.sin(np.deg2rad(self.gun_direction))

        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1

        # ray distance needed to cross one whole tile
        delta_x = abs(1 / dx) if dx != 0 else np.inf
        delta_y = abs(1 / dy) if dy != 0 else np.inf

        # ray distance to the first tile boundary
        tile_x, tile_y = self.tile_x, self.tile_y
        next_x = (tile_x + (step_x > 0) - self.x) / dx if dx != 0 else np.inf
        next_y = (tile_y + (step_y > 0) - self.y) / dy if dy != 0 else np.inf

        t = 0.0
        while 0 <= tile_x < self.map.shape[0] and 0 <= tile_y < self.map.shape[1] and not self.map[tile_x][tile_y]:
            if next_x < next_y:
                t, next_x = next_x, next_x + delta_x
                tile_x += step_x
            else:
                t, next_y = next_y, next_y + delta_y
                tile_y += step_y

        return (float(self.x + dx * t), float(self.y + dy * t))
    
    @property
    def tile_x(self) -> int:
        return int(np.floor(self.x))
    
    @property
    def tile_y(self) -> int:
        return int(np.floor(self.y))
