import game
from ui import console
from ui import entitieswindow
from ui import playerwindow
from ui import levelwindow

from scenes.levelscene import LevelScene
from scenes.scene import Scene
from twitchchatmanager import TwitchChatManager


class GameScene(Scene):
    current_scene = None

    def __init__(self):
        super().__init__()

        self.console = None
        self.level_scene = None
        self.seconds_per_tick = int(game.Game.args.turn) if game.Game.args.turn else 2

        self.init_scene()

    def init_scene(self):
        self.entities.append(TwitchChatManager())
        w = levelwindow.LevelWindow(11, 0, 31, 24, 'Lunch Break RL')
        w.seconds_per_tick = self.seconds_per_tick
        self.entities.append(w)

        self.level_scene = LevelScene()
        self.level_scene.init_scene()
        self.entities.append(self.level_scene)

        w = playerwindow.PlayerWindow(29+13, 0, 11, 30, 'Players')
        self.entities.append(w)

        w = entitieswindow.EntitiesWindow(0, 0, 11, 30)
        self.entities.append(w)

        self.console = console.Console(11, 24, 31, 6, title=None)
        self.entities.append(self.console)

        # Singleton-ish
        if not GameScene.current_scene:
            GameScene.current_scene = self

    @property
    def level(self):
        return self.level_scene.level

