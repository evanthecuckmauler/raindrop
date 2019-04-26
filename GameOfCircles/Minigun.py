from Armored import Armored
from Sprite import Sprite
from Splitter import Splitter
from Player import Player

import SpriteManager

class Minigun(Armored, Sprite):
    armor = 5
    speed = 8
    diameter = 100
    c = color(255, 0, 255)
    mark = 0
    wait = 500
    go = True


    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
    def aim(self, target):
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xComp = target.x - self.x
        yComp = target.y - self.y
        xVec = xComp/2 * .03
        yVec = yComp/2 * .03
        return PVector(xVec, yVec)
    
    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.go = not self.go
            self.mark = millis()
            
        if(self.go):
            self.go = False
            SpriteManager.spawn(Splitter(self.x, self.y, vector, self.team, 10))
