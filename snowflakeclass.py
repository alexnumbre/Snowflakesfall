import random

import wrap
from wrap import sprite,sprite_text

class Snowflake():
    def __init__(self,x,y):
        snowfake=sprite.add("snow", x, y, "snow")
        self.x=x
        self.y=y
        self.id=snowfake
        self.speed=random.randint(2,15)/10


    def movedown(self):
        sprite.move(self.id,0,self.speed)


    def square(self):
        sprite.hide(self.id)
        text=sprite.add_text(str(self.speed),self.x,self.y,back_color=[254,75,255])
        sprite.move(text,self.x,self.y)






