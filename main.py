import pygame as pg
from level import Level
from player import Player
from controller import Controller

class Game:
    def __init__(self) -> None:
        # Pygame init
        self.win = pg.display.set_mode((800, 600), pg.RESIZABLE)
        self.game_surf = pg.Surface((32 * 20, 32 * 15)).convert()
        self.clock = pg.time.Clock()

        # Make and render a level
        self.level = Level()
        self.level.render()

        # Create the user controllers
        self.controller_1 = Controller()
        self.controller_2 = Controller()

        # Create the players
        self.player_1 = Player(self, self.controller_1, None, 2, 7, 45)
        self.player_2 = Player(self, self.controller_2, None, 18, 7)

        # Set the enemies
        self.player_1.enemy = self.player_2
        self.player_2.enemy = self.player_1

    def update(self) -> None:
        ...

    def render(self) -> None:
        # Clear background
        self.win.fill((0, 0, 0, 255))

        # Render game
        self.level.blit_to(self.game_surf)
        self.player_1.render_to(self.game_surf)
        self.player_2.render_to(self.game_surf)


        # Get the blit dims
        win_w, win_h = self.win.get_size()
        game_w, game_h = self.game_surf.get_size()
        scale = min(win_w / game_w, win_h / game_h)
        new_size = (int(game_w * scale), int(game_h * scale))
        scaled = pg.transform.scale(self.game_surf, new_size)

        # Blit the game to the screen as letterbox
        pos = ((win_w - new_size[0]) // 2, (win_h - new_size[1]) // 2)
        self.win.blit(scaled, pos)

        # Update the screen
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

pg.init()
game = Game()
game.run()