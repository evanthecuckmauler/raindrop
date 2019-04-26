import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Minigun import Minigun
from Player import Player
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Armored import Armored

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(600, 600)
    player = Player(width/2, height - 100,1)
    
    SpriteManager.setPlayer(player)
 #   SpriteManager.spawn(Enemy(60, 100, 2))
    SpriteManager.spawn(Minigun(60, 50, 2))

    




                           
def draw():
    background(255)    
    SpriteManager.animate()
    

    
def keyPressed():
    SpriteManager.player.keyDown()
    
def keyReleased():
    SpriteManager.player.keyUp()
