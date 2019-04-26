import SpriteManager

from Sprite import Sprite
from Bullet import Bullet

class Splitter(Sprite):
    diameter = 10
    c = color(0, 255, 0)
    wait2 = 500
    
    def __init__(self, x, y, vector, team, diameter):
        Sprite.__init__(self, x, y, team)
        self.vector = vector
        self.mark2 = millis()
        self.diameter = diameter
        
        
    def split(self):
        if millis() - self.mark2 > self.wait2:

            SpriteManager.destroy(self)
            self.mark2 = millis()
            if self.diameter == 10:
                SpriteManager.destroy(self)
                SpriteManager.spawn(Bullet(self.x, self.y, PVector(self.vector.x-4, self.vector.y-2), self.team))
                SpriteManager.spawn(Bullet(self.x, self.y, PVector(self.vector.x+4, self.vector.y+2), self.team))
    

        
    def move(self):
        self.split()
        self.x += self.vector.x
        self.y += self.vector.y
        if (self.x < 0 - self.diameter
        or self.x > width + self.diameter
        or self.y < 0 - self.diameter
        or self.y > height + self.diameter):
            SpriteManager.destroy(self)
