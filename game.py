# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from panda3d.core import TextNode
from panda3d.core import loadPrcFileData

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land=Mapmanager()
        x,y=self.land.loadLand("land2.txt")
        self.hero=Hero((x//2,y//2,2),self.land)
        base.camLens.setFov(90)

game=Game()
game.run()
