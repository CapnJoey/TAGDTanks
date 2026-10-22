import os
import sys
import random
from math import hypot
import pygame as pg

from game_code.level import Level
from game_code.player import Player
from game_code.user import get_bot_names, User
from game_code.main_menu import MainMenu
from game_code.particles import ParticleSystem
from game_code.win_screen import WinScreen, PauseScreen
from game_code.countdown import Countdown

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

        # Main menu
        self.main_menu = MainMenu(self)

        # Particle system
        self.particle_system = ParticleSystem(self)

        # Bullet array
        self.bullets = []

        # Screen shake
        self.shake_timer = 0.0
        self.shake_intensity = 4

        # Peggle zoom
        self.zoom = 1.0
        self.max_zoom = 1.75
        self.zoom_radius = 1.5
        self.zoom_focus = (10, 7.5)
        self.time_scale = 1.0
        self.real_dt = 0

        self.game_over = False
        self.win_screen = None
        self.pause_screen = None
        self.countdown = Countdown()

        # Letterbox transform, used to map window mouse positions onto the game surface
        self.view_scale = 1.0
        self.view_pos = (0, 0)

    def to_surface_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        return (int((pos[0] - self.view_pos[0]) / self.view_scale),
                int((pos[1] - self.view_pos[1]) / self.view_scale))

    def start_match(self, name_1: str, name_2: str) -> None:
        # Reset match state
        self.bullets = []
        self.particle_system.particles = []
        self.shake_timer = 0.0
        self.zoom = 1.0
        self.time_scale = 1.0
        self.game_over = False
        self.win_screen = None
        self.pause_screen = None
        self.countdown = Countdown()

        # Load users
        self.user_1 = User(name_1)
        self.user_2 = User(name_2)

        # Create the players
        self.player_1 = Player(self, self.user_1, None, 2, 7, 0, 1)
        self.player_2 = Player(self, self.user_2, None, 18, 7, 180, 2)

        # Set the enemies
        self.player_1.enemy = self.player_2
        self.player_2.enemy = self.player_1

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

    def toggle_pause(self) -> None:
        if self.win_screen:
            return
        self.pause_screen = None if self.pause_screen else PauseScreen()

    def update(self) -> None:
        if self.pause_screen:
            self.pause_screen.update(self.real_dt)
            return

        self.countdown.update(self.real_dt)
        if self.countdown.blocking:
            return

        self.shake_timer = max(0.0, self.shake_timer - self.dt)
        self.update_zoom()

        self.player_1.update()
        self.player_2.update()
        self.particle_system.update()

        dead = []
        for bullet in self.bullets:
            bullet.update([self.player_1, self.player_2], self.level.map, self.dt)
            if bullet.dead:
                dead.append(bullet)

        for bullet in dead:
            self.bullets.remove(bullet)

        if self.game_over and self.win_screen is None:
            winner = self.player_1 if self.player_1.alive else self.player_2
            self.win_screen = WinScreen(winner.user.name)
        if self.win_screen:
            self.win_screen.update(self.real_dt)

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

        self.particle_system.render(self.game_surf)

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

        # Draw overlays over the final view, unaffected by zoom
        overlay = self.pause_screen or self.win_screen
        if overlay or not self.countdown.done:
            if view is self.game_surf:
                view = pg.Surface((game_w, game_h)).convert()
                view.blit(self.game_surf, (0, 0))
            else:
                view = pg.transform.scale(view, (game_w, game_h))
            self.countdown.render(view)
            if overlay:
                overlay.render(view, self.to_surface_pos(pg.mouse.get_pos()))

        scaled = pg.transform.scale(view, new_size)

        # Blit the game to the screen as letterbox
        pos = ((win_w - new_size[0]) // 2, (win_h - new_size[1]) // 2)
        self.view_scale = scale
        self.view_pos = pos
        if self.shake_timer > 0 and not self.pause_screen:
            pos = (pos[0] + random.randint(-self.shake_intensity, self.shake_intensity),
                   pos[1] + random.randint(-self.shake_intensity, self.shake_intensity))
        self.win.blit(scaled, pos)

        # Update the screen
        pg.display.flip()

    def run(self) -> None:
        self.running = True
        show_menu = True
        while self.running:
            if show_menu:
                self.main_menu.run()
                if not self.running:
                    return
            self.start_match(*self.main_menu.selected_names)
            show_menu = self.play_match()

    def play_match(self) -> bool:
        """Runs one match. Returns True if the player chose to go back to the main menu."""
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.toggle_pause()
                overlay = self.pause_screen or self.win_screen
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and overlay:
                    overlay.handle_click(self.to_surface_pos(event.pos))

            self.real_dt = self.clock.tick(60) / 1000.0
            self.dt = self.real_dt * self.time_scale

            self.update()
            self.render()

            overlay = self.pause_screen or self.win_screen
            if overlay and overlay.choice:
                return overlay.choice == "main_menu"
        return False

pg.init()
game = Game()
game.run()