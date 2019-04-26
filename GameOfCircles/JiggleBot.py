import SpriteManager 
from Armored import Armored
from Sprite import Sprite
from Bullet import Bullet

class JiggleBot(Armored, Sprite):
    
    armor = 4
    speed = 8
    diameter = 50
    c = color(255,255,0)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.speed += 0.01
        self.x += random(-self.speed, self.speed)
        self.y += random(-self.speed, self.speed)
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
