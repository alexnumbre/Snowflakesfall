import random

import wrap
from wrap import sprite,sprite_text


class Snowflake():
    def __init__(self,x,y,mode=True):
        self.speed=random.randint(2,15)/5
        self.mode=mode
        self.id=sprite.add("snow", x, y, "snow",visible=mode)
        self.text = sprite.add_text(str(self.speed), x, y, back_color=[254, 75, 255],visible=not mode)


    def movedown(self):
        sprite.move(self.id,0,self.speed)
        sprite.move(self.text,0,self.speed)



    def square(self):
        if not self.mode:
            return

        sprite.hide(self.id)
        sprite.show(self.text)
        self.mode=False


    def normal(self):
        if self.mode:
            return

        sprite.show(self.id)
        sprite.hide(self.text)
        self.mode=True






