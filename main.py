import pygame as pg
from level import Level

class Game:
    def __init__(self) -> None:
        # Pygame init
        self.win = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()

        self.level = Level()
        self.level.render()

        self.player_1 = None
        self.player_2 = None

    def update(self) -> None:
        ...

    def render(self) -> None:
        # Clear background
        self.win.fill((0, 0, 0, 1))

        # Render 
        self.level.blit_to(self.win)

        pg.display.flip()

    def run(self) -> None:
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            self.clock.tick(60)

            self.update()
            self.render()
            print("test")

pg.init()
game = Game()
game.run()