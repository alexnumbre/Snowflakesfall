import random

import wrap
from wrap import world,sprite

wrap.add_sprite_dir("MySprites")

world.create_world(700,700)
world.set_back_color(0,180,100)
snowlist=[]

@wrap.always(1000)
def snowfall():
    x= random.randint(20,680)
    y=-5
    snowflake=sprite.add("snow",x,y,"snow")
    snowlist.append(snowflake)



@wrap.always(50)
def speedsnowflake():
    for snowflake in snowlist:
        sprite.move(snowflake,0,8)




