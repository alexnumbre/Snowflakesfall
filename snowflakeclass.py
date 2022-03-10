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
        self.mode=True


    def movedown(self):
        sprite.move(self.id,0,self.speed)
        if self.mode==False:
            sprite.move(self.text,0,self.speed)



    def square(self):
        if self.mode == False:
            return


        xnow=sprite.get_x(self.id)
        ynow=sprite.get_y(self.id)

        sprite.hide(self.id)
        self.text=sprite.add_text(str(self.speed),xnow,ynow,back_color=[254,75,255])
        self.mode=False


    def normal(self):

        sprite.show(self.id)
        sprite.hide(self.text)
        self.mode=True

#превращается только ожна снежинка, почему?





