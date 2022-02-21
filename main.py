import random,snowflake

import wrap
from wrap import world,sprite

wrap.add_sprite_dir("MySprites")

world.create_world(700,700)
world.set_back_color(150,215,255)
snowlist=[]

@wrap.always(1000)
def snowflake2():
    snowlist.append(snowflake.createsnowflake())




@wrap.always(50)
def speedsnowflake():
    for snowlake in snowlist:
        sprite.move(snowlake["id"],0,snowlake["speed"])







