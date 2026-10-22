import pygame as pg

# Each tank gets two reserved channels (engine loop + windup) so its movement
# sounds can be stopped without touching anything else that is playing.
CHANNELS_PER_TANK = 2
MAX_TANKS = 2

_sounds: dict[str, pg.mixer.Sound] = {}
_enabled = False


def init() -> None:
    """Load all sound effects. Safe to call if no audio device is available."""
    global _enabled
    try:
        if not pg.mixer.get_init():
            pg.mixer.init()
        pg.mixer.set_num_channels(16)
        pg.mixer.set_reserved(CHANNELS_PER_TANK * MAX_TANKS)
        for name in ("sndShootLight", "sndShootHeavy", "tankloop", "tankwindup"):
            _sounds[name] = pg.mixer.Sound(f"./assets/{name}.wav")
        _enabled = True
    except pg.error as e:
        print("Sound disabled: ", e)
        _enabled = False


def play(name: str) -> None:
    """Play a one-shot sound effect on any free channel."""
    if _enabled:
        _sounds[name].play()


class TankEngineSound:
    """Plays the windup + engine loop while a tank drives in one direction."""

    def __init__(self, tag: int) -> None:
        self.direction = None
        self.loop_channel = None
        self.windup_channel = None
        if _enabled:
            base = (tag - 1) % MAX_TANKS * CHANNELS_PER_TANK
            self.loop_channel = pg.mixer.Channel(base)
            self.windup_channel = pg.mixer.Channel(base + 1)

    def update(self, direction: str | None) -> None:
        """direction is 'forward', 'backward' or None (not driving)."""
        if direction == self.direction:
            return
        self.stop()
        self.direction = direction
        if direction and _enabled:
            self.windup_channel.play(_sounds["tankwindup"])
            self.loop_channel.play(_sounds["tankloop"], loops=-1)

    def stop(self) -> None:
        self.direction = None
        if _enabled:
            self.loop_channel.stop()
            self.windup_channel.stop()

