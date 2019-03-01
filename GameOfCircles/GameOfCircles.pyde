import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    player = Player(width/2, height - 100,1)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(Enemy(100, 100, 2))
    SpriteManager.spawn(Raindrop(200, 50, 2))
                           
def draw():
    background(255)    
    SpriteManager.animate()
    

    
def keyPressed():
    SpriteManager.player.keyDown()
    
def keyReleased():
    SpriteManager.player.keyUp()
