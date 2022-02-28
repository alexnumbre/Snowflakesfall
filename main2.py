import random,snowflakeclass

import wrap
from wrap import world,sprite

wrap.add_sprite_dir("MySprites")

world.create_world(700,700)
world.set_back_color(150,215,255)
snowlist=[]

@wrap.always(1000)
def snowflake():
    snowlist.append(snowflakeclass.Snowflake(random.randint(20,680),-5))

@wrap.always(10)
def down():
    for snowflake in snowlist:
        snowflake.movedown()

@wrap.on_key_down(wrap.K_SPACE)
def square():
    for snowflake in snowlist:
        snowflake.square()