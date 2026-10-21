import random
from math import hypot
import pygame as pg
from level import Level
from player import Player
from controller import Controller, HumanControllerLeft, HumanControllerRight
from test_ai import Gilbert, TestTank

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
        self.controller_1 = Gilbert()
        self.controller_2 = Gilbert()

        # Create the players
        self.player_1 = Player(self, self.controller_1, None, 2, 7, 0, 1)
        self.player_2 = Player(self, self.controller_2, None, 18, 7, 180, 2)

        # Set the enemies
        self.player_1.enemy = self.player_2
        self.player_2.enemy = self.player_1

        # Bullet array
        self.bullets = []

        # Screen shake
        self.shake_timer = 0.0
        self.shake_intensity = 3

        # Peggle zoom
        self.zoom = 1.0
        self.max_zoom = 2.0
        self.zoom_radius = 2.0
        self.zoom_focus = (10, 7.5)
        self.time_scale = 1.0
        self.real_dt = 0

    def update_zoom(self) -> None:
        closest = None
        for bullet in self.bullets:
            for player in (self.player_1, self.player_2):
                if player.tag == bullet.tag:
                    continue
                d = hypot(bullet.x - player.x, bullet.y - player.y)
                if d < self.zoom_radius and (closest is None or d < closest[0]):
                    closest = (d, bullet, player)

        target_zoom = 1.0
        if closest:
            _, bullet, player = closest
            target_zoom = self.max_zoom
            self.zoom_focus = ((bullet.x + player.x) / 2, (bullet.y + player.y) / 2)

        self.zoom += (target_zoom - self.zoom) * min(1.0, 8 * self.real_dt)
        self.time_scale = 1.0 - 0.65 * (self.zoom - 1.0) / (self.max_zoom - 1.0)

    def update(self) -> None:
        self.shake_timer = max(0.0, self.shake_timer - self.dt)
        self.update_zoom()

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
        if self.player_1.y > self.player_2.y:
            self.player_1.render_to(self.game_surf)
            self.player_2.render_to(self.game_surf)
        else:
            self.player_2.render_to(self.game_surf)
            self.player_1.render_to(self.game_surf)

        for bullet in self.bullets:
            bullet.render_to(self.game_surf)


        # Get the blit dims
        win_w, win_h = self.win.get_size()
        game_w, game_h = self.game_surf.get_size()
        scale = min(win_w / game_w, win_h / game_h)
        new_size = (int(game_w * scale), int(game_h * scale))
        view = self.game_surf
        if self.zoom > 1.001:
            view_w = max(1, int(game_w / self.zoom))
            view_h = max(1, int(game_h / self.zoom))
            fx, fy = self.zoom_focus[0] * 32, (15 - self.zoom_focus[1]) * 32
            left = int(min(max(fx - view_w / 2, 0), game_w - view_w))
            top = int(min(max(fy - view_h / 2, 0), game_h - view_h))
            view = pg.Surface((view_w, view_h)).convert()
            view.blit(self.game_surf, (0, 0), pg.Rect(left, top, view_w, view_h))
        scaled = pg.transform.scale(view, new_size)

        # Blit the game to the screen as letterbox
        pos = ((win_w - new_size[0]) // 2, (win_h - new_size[1]) // 2)
        if self.shake_timer > 0:
            pos = (pos[0] + random.randint(-self.shake_intensity, self.shake_intensity),
                   pos[1] + random.randint(-self.shake_intensity, self.shake_intensity))
        self.win.blit(scaled, pos)

        # Update the screen
        pg.display.flip()

    def run(self) -> None:
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            self.real_dt = self.clock.tick(60) / 1000.0
            self.dt = self.real_dt * self.time_scale

            self.update()
            self.render()

pg.init()
game = Game()
game.run()