import pygame as pg


class Player:
    def __init__(self, start_x: float=1.0, start_y: float=1.0) -> None:
        self.x = start_x
        self.y = start_y
