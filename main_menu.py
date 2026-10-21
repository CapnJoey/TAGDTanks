import pygame as pg
from user import get_bot_names

TEXT_COLOR = pg.Color("#c5ccb8")
OUTLINE_COLOR = pg.Color("#433455")
BOX_COLOR = pg.Color("#6a998a")
BOX_HOVER_COLOR = pg.Color("#84b3a4")


def render_box(surf: pg.Surface, font: pg.font.Font, rect: pg.Rect, label: str,
               highlight: bool, centered: bool = False) -> None:
    pg.draw.rect(surf, BOX_HOVER_COLOR if highlight else BOX_COLOR, rect)
    pg.draw.rect(surf, OUTLINE_COLOR, rect, 2)

    text = font.render(label, True, TEXT_COLOR)
    font.outline = 1
    outline = font.render(label, True, OUTLINE_COLOR)
    font.outline = 0

    if centered:
        text_center = rect.center
    else:
        text_center = (rect.x + 7 + text.get_width() // 2, rect.centery)
    surf.blit(outline, outline.get_rect(center=text_center))
    surf.blit(text, text.get_rect(center=text_center))


class Dropdown:
    def __init__(self, rect: pg.Rect, options: list[str], selected: int = 0) -> None:
        self.rect = pg.Rect(rect)
        self.options = options
        self.selected = selected
        self.open = False

    @property
    def value(self) -> str:
        return self.options[self.selected]

    def option_rect(self, i: int) -> pg.Rect:
        return self.rect.move(0, self.rect.height * (i + 1))

    def handle_click(self, pos: tuple[int, int]) -> bool:
        """Returns True if the click was consumed by this dropdown"""
        if self.rect.collidepoint(pos):
            self.open = not self.open
            return True
        if self.open:
            self.open = False
            for i in range(len(self.options)):
                if self.option_rect(i).collidepoint(pos):
                    self.selected = i
                    return True
        return False

    def render(self, surf: pg.Surface, font: pg.font.Font, mouse: tuple[int, int]) -> None:
        render_box(surf, font, self.rect, self.value, self.rect.collidepoint(mouse))
        arrow_x, arrow_y = self.rect.right - 11, self.rect.centery
        points = [(arrow_x - 4, arrow_y - 2), (arrow_x + 4, arrow_y - 2), (arrow_x, arrow_y + 2)]
        pg.draw.polygon(surf, OUTLINE_COLOR, points)

        if self.open:
            for i, option in enumerate(self.options):
                rect = self.option_rect(i)
                render_box(surf, font, rect, option, rect.collidepoint(mouse) or i == self.selected)


class MainMenu:
    def __init__(self, game) -> None:
        self.game = game

        self.surface = pg.Surface((640, 480))
        self.font = pg.font.Font("./assets/upheavtt.ttf", 20)
        self.dropdown_font = self.font

        self.bg = pg.image.load("./assets/bg.png").convert()
        self.logo = pg.image.load("./assets/logo.png").convert_alpha()

        # Character select
        names = get_bot_names()
        default_1 = names.index("Player1") if "Player1" in names else 0
        default_2 = names.index("Gilbert") if "Gilbert" in names else min(1, len(names) - 1)
        self.dropdowns = [
            Dropdown(pg.Rect(105, 304, 150, 22), names, default_1),
            Dropdown(pg.Rect(385, 304, 150, 22), names, default_2),
        ]
        self.start_button = pg.Rect(245, 400, 150, 40)

        # Letterbox transform, used to map window mouse positions onto the menu surface
        self.view_scale = 1.0
        self.view_pos = (0, 0)

    @property
    def selected_names(self) -> tuple[str, str]:
        return self.dropdowns[0].value, self.dropdowns[1].value

    def to_surface_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        return (int((pos[0] - self.view_pos[0]) / self.view_scale),
                int((pos[1] - self.view_pos[1]) / self.view_scale))

    def render(self) -> None:
        self.surface.fill((0, 0, 0))

        # Blit the background
        self.surface.blit(self.bg, (0, 0))

        # Render the logo in the center of the screen, scaled up
        logo_w, logo_h = self.logo.get_size()
        scale = 0.6 * min(self.surface.get_width() / logo_w, self.surface.get_height() / logo_h)
        new_size = (int(logo_w * scale), int(logo_h * scale))
        logo = pg.transform.scale(self.logo, new_size)
        surf_rect = self.surface.get_rect()
        logo_rect = logo.get_rect(center=(surf_rect.centerx, surf_rect.height // 4))
        self.surface.blit(logo, logo_rect.clamp(surf_rect))

        # Character select
        mouse = self.to_surface_pos(pg.mouse.get_pos())

        # Start button
        hover = self.start_button.collidepoint(mouse) and not any(d.open for d in self.dropdowns)
        render_box(self.surface, self.font, self.start_button, "Start", hover, centered=True)

        # Draw open dropdowns last so their lists overlap everything else
        for dropdown in sorted(self.dropdowns, key=lambda d: d.open):
            dropdown.render(self.surface, self.dropdown_font, mouse)

        # Get the blit dims
        win_w, win_h = self.game.win.get_size()
        game_w, game_h = self.surface.get_size()
        scale = min(win_w / game_w, win_h / game_h)
        new_size = (int(game_w * scale), int(game_h * scale))
        view = self.surface
        scaled = pg.transform.scale(view, new_size)

        # Blit the game to the screen as letterbox
        pos = ((win_w - new_size[0]) // 2, (win_h - new_size[1]) // 2)
        self.view_scale = scale
        self.view_pos = pos
        self.game.win.blit(scaled, pos)
        pg.display.flip()

    def handle_click(self, pos: tuple[int, int]) -> None:
        pos = self.to_surface_pos(pos)
        was_open = any(d.open for d in self.dropdowns)

        # An open dropdown gets first pick so its list can cover other widgets
        for dropdown in sorted(self.dropdowns, key=lambda d: not d.open):
            if dropdown.handle_click(pos):
                for other in self.dropdowns:
                    if other is not dropdown:
                        other.open = False
                return

        # Clicking outside an open dropdown only closes it
        if was_open:
            return

        if self.start_button.collidepoint(pos):
            self.running = False

    def update(self) -> None:
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE] or keys[pg.K_RETURN]:
            self.running = False
            return

    def run(self) -> None:
        self.running = True
        while self.game.running and self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                    return
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)

            self.game.clock.tick(60)

            self.update()
            self.render()
