import pygame as pg
from game_code.main_menu import TEXT_COLOR, OUTLINE_COLOR


class Countdown:
    STEP_TIME = 0.35
    FIGHT_TIME = 0.6
    STEPS = ("3", "2", "1")

    def __init__(self) -> None:
        self.timer = 0.0
        self.font = pg.font.Font("./assets/upheavtt.ttf", 80)
        self.font.outline = 3
        outlines = {label: self.font.render(label, True, OUTLINE_COLOR) for label in (*self.STEPS, "FIGHT!")}
        self.font.outline = 0
        self.labels = {
            label: self._compose(self.font.render(label, True, TEXT_COLOR), outline)
            for label, outline in outlines.items()
        }

    @staticmethod
    def _compose(text: pg.Surface, outline: pg.Surface) -> pg.Surface:
        surf = outline.copy()
        surf.blit(text, text.get_rect(center=surf.get_rect().center))
        return surf

    @property
    def blocking(self) -> bool:
        """True while gameplay should be frozen"""
        return self.timer < self.STEP_TIME * len(self.STEPS)

    @property
    def done(self) -> bool:
        return self.timer >= self.STEP_TIME * len(self.STEPS) + self.FIGHT_TIME

    def update(self, real_dt: float) -> None:
        self.timer += real_dt

    def render(self, surf: pg.Surface) -> None:
        if self.done:
            return

        step = int(self.timer // self.STEP_TIME)
        if step < len(self.STEPS):
            label = self.STEPS[step]
            t = (self.timer % self.STEP_TIME) / self.STEP_TIME
            alpha = 255
        else:
            label = "FIGHT!"
            t = (self.timer - self.STEP_TIME * len(self.STEPS)) / self.FIGHT_TIME
            alpha = int(255 * min(1.0, 2 * (1 - t)))

        # Pop in large and settle to normal size
        scale = 1 + 0.6 * max(0.0, 1 - t / 0.4) ** 2
        image = self.labels[label]
        image = pg.transform.scale_by(image, scale)
        image.set_alpha(alpha)
        surf.blit(image, image.get_rect(center=surf.get_rect().center))
