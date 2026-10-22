import math
import pygame as pg
from game_code.countdown import render_outlined, pop_in


class MatchTimer:
    # (duration in seconds, popup lines shown when the phase starts). The last phase never ends.
    PHASES = [
        (60.0, None),
        (30.0, ("SUDDEN", "DEATH")),
        (None, ("SUDDENER", "DEATH")),
    ]
    POPUP_TIME = 1.5  # how long a phase popup stays on screen

    def __init__(self) -> None:
        self.phase = 0
        self.remaining = self.PHASES[0][0]
        self.popup_timer = 0.0

        self.font = pg.font.Font("./assets/upheavtt.ttf", 40)
        popup_font = pg.font.Font("./assets/upheavtt.ttf", 80)
        self.popups = [
            [render_outlined(popup_font, line, 3) for line in lines] if lines else None
            for _, lines in self.PHASES
        ]

    def update(self, real_dt: float) -> int | None:
        """Returns the new phase index on the frame a phase starts"""
        self.popup_timer += real_dt
        if self.remaining is None:
            return None

        self.remaining = max(0.0, self.remaining - real_dt)
        if self.remaining > 0:
            return None

        self.phase += 1
        self.remaining = self.PHASES[self.phase][0]
        self.popup_timer = 0.0
        return self.phase

    def render(self, surf: pg.Surface) -> None:
        width, height = surf.get_size()

        # Seconds left in this phase, top middle
        seconds = 0 if self.remaining is None else math.ceil(self.remaining)
        label = render_outlined(self.font, str(seconds), 2)
        surf.blit(label, label.get_rect(midtop=(width // 2, 8)))

        # Popup for the phase that just started
        popup = self.popups[self.phase]
        if popup and self.popup_timer < self.POPUP_TIME:
            t = self.popup_timer / self.POPUP_TIME
            alpha = int(255 * min(1.0, 2 * (1 - t)))
            line_height = popup[0].get_height()
            for i, line in enumerate(popup):
                center = (width // 2, height // 2 + int((i - (len(popup) - 1) / 2) * line_height))
                pop_in(surf, line, t, alpha, center)
