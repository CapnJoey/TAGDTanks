import numpy as np

class Controller:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
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



        # END YOUR CODE HERE


    def turn_body_left(self): 
        self.body_turn_action = "left"

    def turn_body_right(self):
        self.body_turn_action = "right"
    
    def stop_turn_body(self):
        self.body_turn_action = None

    def turn_gun_left(self):
        self.gun_turn_action = "left"

    def turn_gun_right(self):
        self.gun_turn_action = "right"

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