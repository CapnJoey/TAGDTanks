import pygame as pg
from level import Level

class Game:
    def __init__(self) -> None:
        # Pygame init
        self.win = pg.display.set_mode((800, 600), pg.RESIZABLE)
        self.game_surf = pg.Surface((32 * 20, 32 * 15)).convert()
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
        self.level.blit_to(self.game_surf)

        # Get the blit dims
        win_w, win_h = self.win.get_size()
        game_w, game_h = self.game_surf.get_size()
        scale = min(win_w / game_w, win_h / game_h)
        new_size = (int(game_w * scale), int(game_h * scale))
        scaled = pg.transform.scale(self.game_surf, new_size)

        # Blit the game to the screen as letterbox
        pos = ((win_w - new_size[0]) // 2, (win_h - new_size[1]) // 2)
        self.win.blit(scaled, pos)


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