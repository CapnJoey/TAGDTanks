import numpy as np
import pygame as pg

class Controller:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.enemy_x = 0
        self.enemy_y = 0
        self.body_direction = 0
        self.gun_direction = 0
        self.map = np.zeros((20, 15))

        self.body_turn_action = None
        self.gun_turn_action = None
        self.move_action = None
        self.shoot_action = False

        # DEFINE CUSTOM STATE VARIABLES (optional)



        # END DEFINE CUSTOM STATE VARIABLES (optional)

    def update(self):
        """
        TODO
        """

        # START YOUR CODE HERE

        self.move_forward()
        self.turn_body_clockwise()
        # self.turn_gun_counter_clockwise()

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


class HumanControllerLeft(Controller):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]: self.move_forward()
        if keys[pg.K_s]: self.move_backward()
        if keys[pg.K_a]: self.turn_body_counter_clockwise()
        if keys[pg.K_d]: self.turn_body_clockwise()
        if keys[pg.K_q]: self.turn_gun_counter_clockwise()
        if keys[pg.K_e]: self.turn_gun_clockwise()
        if keys[pg.K_LSHIFT]: self.shoot()

class HumanControllerRight(Controller):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_i]: self.move_forward()
        if keys[pg.K_k]: self.move_backward()
        if keys[pg.K_j]: self.turn_body_counter_clockwise()
        if keys[pg.K_l]: self.turn_body_clockwise()
        if keys[pg.K_u]: self.turn_gun_counter_clockwise()
        if keys[pg.K_o]: self.turn_gun_clockwise()
        if keys[pg.K_RETURN]: self.shoot()
