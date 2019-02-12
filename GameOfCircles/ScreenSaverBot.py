class ScreenSaverBot:
   
    xspeed = 8
    yspeed = 4
    diameter = 50
    c = color(0,255,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x > width or self.x < 0:
            self.xspeed *= -1
        if self.y > height or self.y < 0:
            self.yspeed *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
