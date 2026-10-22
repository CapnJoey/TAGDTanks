import pygame as pg
from main_menu import TEXT_COLOR, render_box


def ease_out(t: float) -> float:
    t = min(max(t, 0.0), 1.0)
    return 1 - (1 - t) ** 3


class WinScreen:
    # Seconds after the kill at which each stage starts, and how long it takes
    DELAY = 0.6
    DIM_TIME = 0.4
    BAR_TIME = 0.5
    BUTTON_TIME = 0.5

    def __init__(self, winner_name: str) -> None:
        self.winner_name = winner_name
        self.timer = 0.0
        self.choice = None  # "play_again" or "main_menu" once clicked

        self.font = pg.font.Font("./assets/upheavtt.ttf", 20)
        self.title_font = pg.font.Font("./assets/upheavtt.ttf", 40)

        self.bar_height = 70
        self.bar_y = 170
        self.buttons = {
            "play_again": ("Play Again", pg.Rect(150, 300, 150, 40)),
            "main_menu": ("Main Menu", pg.Rect(340, 300, 150, 40)),
        }

    def progress(self, stage: int) -> float:
        """0 to 1 progress of the dim (0), bar (1) and button (2) animations"""
        durations = (self.DIM_TIME, self.BAR_TIME, self.BUTTON_TIME)
        start = self.DELAY + sum(durations[:stage])
        return min(max((self.timer - start) / durations[stage], 0.0), 1.0)

    @property
    def buttons_ready(self) -> bool:
        return self.progress(2) >= 1.0

    def update(self, real_dt: float) -> None:
        self.timer += real_dt

    def handle_click(self, pos: tuple[int, int]) -> None:
        if not self.buttons_ready:
            return
        for key, (_, rect) in self.buttons.items():
            if rect.collidepoint(pos):
                self.choice = key

    def render(self, surf: pg.Surface, mouse: tuple[int, int]) -> None:
        width, height = surf.get_size()

        # Dim the game
        dim = self.progress(0)
        if dim > 0:
            overlay = pg.Surface((width, height), pg.SRCALPHA)
            overlay.fill((0, 0, 0, int(150 * dim)))
            surf.blit(overlay, (0, 0))

        # Slide the bar in from the left
        bar = ease_out(self.progress(1))
        if bar > 0:
            offset = int((bar - 1) * width)
            bar_rect = pg.Rect(offset, self.bar_y, width, self.bar_height)
            bar_surf = pg.Surface(bar_rect.size, pg.SRCALPHA)
            bar_surf.fill((0, 0, 0, 180))
            surf.blit(bar_surf, bar_rect)
            text = self.title_font.render(f"{self.winner_name} wins", True, TEXT_COLOR)
            surf.blit(text, text.get_rect(center=bar_rect.center))

        # Slide the buttons up from the bottom
        rise = ease_out(self.progress(2))
        if rise > 0:
            for label, rect in self.buttons.values():
                start_y = height + 10
                drawn = rect.move(0, int((start_y - rect.y) * (1 - rise)))
                hover = self.buttons_ready and drawn.collidepoint(mouse)
                render_box(surf, self.font, drawn, label, hover, centered=True)
