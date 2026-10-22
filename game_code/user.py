import os
import importlib.util
import pygame as pg


def get_bot_names(bots_dir: str = "./bots/") -> list[str]:
    return sorted(
        entry.name for entry in os.scandir(bots_dir)
        if entry.is_dir() and not entry.name.startswith((".", "__"))
    )


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.directory = f"./bots/{name}/"

        path = os.path.join(self.directory, "controller.py")
        spec = importlib.util.spec_from_file_location(f"bots.{name}.controller", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self.controller = module.Controller()

        # Load the tank images
        self.tank_images = [
            pg.image.load(os.path.join(self.directory, f"tank{i+1}.png")).convert_alpha() for i in range(4)
        ]
        self.tank_images = [pg.transform.scale(image, (32, 32)) for image in self.tank_images]

        # Load gun images
        self.gun_images = [
            pg.image.load(os.path.join(self.directory, f"gun{i+1}.png")).convert_alpha() for i in range(4)
        ]
        self.gun_images = [pg.transform.scale(image, (32, 32)) for image in self.gun_images]

        # Load the bullet image
        self.bullet_image = pg.image.load(os.path.join(self.directory, "bullet.png")).convert_alpha()
        self.bullet_image = pg.transform.scale(self.bullet_image, (32, 32))
