import numpy as np
import pygame as pg
import random
import game_code.cheat_prevention

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
