import os
import ast
import importlib.util
import pygame as pg

REQUIRED_IMPORT = "from game_code.cheat_prevention import *"


def has_cheat_prevention(source: str) -> bool:
    """True if the source imports cheat_prevention at module level"""
    for node in ast.parse(source).body:
        if (isinstance(node, ast.ImportFrom) and node.module == "game_code.cheat_prevention"
                and node.level == 0 and any(alias.name == "*" for alias in node.names)):
            return True
    return False


BANNED_MODULES = {"builtins", "importlib"}
# Anything that can look up a name from a string could be used to rebuild `__self__` etc.
BANNED_NAMES = {"__builtins__", "__import__", "getattr", "setattr", "delattr", "eval", "exec",
                "compile", "globals", "vars", "open"}
ALLOWED_DUNDER_ATTRIBUTES = {"__init__"}


def find_banned_code(source: str) -> list[str]:
    """Returns a description of every way the source tries to reach the builtins module"""
    problems = []
    for node in ast.walk(ast.parse(source)):
        line = getattr(node, "lineno", "?")
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in BANNED_MODULES:
                    problems.append(f"line {line}: imports `{alias.name}`")
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in BANNED_MODULES:
                problems.append(f"line {line}: imports from `{node.module}`")
        elif isinstance(node, ast.Name) and node.id in BANNED_NAMES:
            problems.append(f"line {line}: uses `{node.id}`")
        elif isinstance(node, ast.Attribute) and node.attr.startswith("__") \
                and node.attr not in ALLOWED_DUNDER_ATTRIBUTES:
            # e.g. `len.__self__` is the builtins module
            problems.append(f"line {line}: accesses `.{node.attr}`")
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) and "builtins" in node.value:
            # e.g. `sys.modules["builtins"]` or `getattr(x, "__builtins__")`
            problems.append(f"line {line}: mentions \"builtins\" in a string")
    return problems


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
        with open(path) as file:
            source = file.read()
        if not has_cheat_prevention(source):
            raise ImportError(f"Bot '{name}' is missing the line `{REQUIRED_IMPORT}` in {path}")
        problems = find_banned_code(source)
        if problems:
            raise ImportError(f"Bot '{name}' tries to access builtins in {path}:\n  " + "\n  ".join(problems))

        spec = importlib.util.spec_from_file_location(f"bots.{name}.controller", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self.controller = module.Controller()

        # Animation frames first, idle image last (Player indexes them that way)
        self.tank_images = [self.load_image(f"tank_move_{i}") for i in range(1, 4)] + [self.load_image("tank_idle")]
        self.gun_images = [self.load_image(f"gun_shoot_{i}") for i in range(1, 4)] + [self.load_image("gun_idle")]
        self.bullet_image = self.load_image("bullet")

    def load_image(self, name: str) -> pg.Surface:
        image = pg.image.load(os.path.join(self.directory, f"{name}.png")).convert_alpha()
        return pg.transform.scale(image, (32, 32))
