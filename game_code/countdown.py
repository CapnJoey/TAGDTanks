import pygame as pg
from game_code.main_menu import TEXT_COLOR, OUTLINE_COLOR


def render_outlined(font: pg.font.Font, label: str, outline: int) -> pg.Surface:
    """Renders label in the UI text colour with a solid outline around it"""
    font.outline = outline
    surf = font.render(label, True, OUTLINE_COLOR)
    font.outline = 0
    text = font.render(label, True, TEXT_COLOR)
    surf.blit(text, text.get_rect(center=surf.get_rect().center))
    return surf


def pop_in(surf: pg.Surface, image: pg.Surface, t: float, alpha: int, center: tuple[int, int]) -> None:
    """Blits image starting large and settling to normal size over the first 40% of t"""
    scale = 1 + 0.6 * max(0.0, 1 - t / 0.4) ** 2
    image = pg.transform.scale_by(image, scale)
    image.set_alpha(alpha)
    surf.blit(image, image.get_rect(center=center))


class Countdown:
    STEP_TIME = 0.35
    FIGHT_TIME = 0.6
    STEPS = ("3", "2", "1")

    def __init__(self) -> None:
        self.timer = 0.0
        self.font = pg.font.Font("./assets/upheavtt.ttf", 80)
        self.labels = {label: render_outlined(self.font, label, 3) for label in (*self.STEPS, "FIGHT!")}

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

        pop_in(surf, self.labels[label], t, alpha, surf.get_rect().center)
