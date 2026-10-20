import pygame as pg
from level import Level
from player import Player
from controller import Controller, HumanControllerLeft, HumanControllerRight

class Game:
    def __init__(self) -> None:
        # Pygame init
        self.win = pg.display.set_mode((800, 600), pg.RESIZABLE)
        self.game_surf = pg.Surface((32 * 20, 32 * 15)).convert()
        self.clock = pg.time.Clock()
        self.dt = 0

        # Make and render a level
        self.level = Level()
        self.level.render()

        # Create the user controllers
        self.controller_1 = HumanControllerLeft()
        self.controller_2 = HumanControllerRight()

        # Create the players
        self.player_1 = Player(self, self.controller_1, None, 2, 7, 0, 1)
        self.player_2 = Player(self, self.controller_2, None, 18, 7, 180, 2)

        # Set the enemies
        self.player_1.enemy = self.player_2
        self.player_2.enemy = self.player_1

        # Bullet array
        self.bullets = []

    def update(self) -> None:
        self.player_1.update()
        self.player_2.update()

        dead = []
        for bullet in self.bullets:
            bullet.update([self.player_1, self.player_2], self.level.map, self.dt)
            if bullet.dead:
                dead.append(bullet)

        for bullet in dead:
            self.bullets.remove(bullet)

    def render(self) -> None:
        # Clear background
        self.win.fill((0, 0, 0, 255))

        # Render game
        self.level.blit_to(self.game_surf)
        self.player_1.render_to(self.game_surf)
        self.player_2.render_to(self.game_surf)

        for bullet in self.bullets:
            bullet.render_to(self.game_surf)


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
            
            self.dt = self.clock.tick(60) / 1000.0

            self.update()
            self.render()

pg.init()
game = Game()
game.run()