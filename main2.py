import random, snowflakeclass

import wrap
from wrap import world, sprite

import drop

wrap.add_sprite_dir("MySprites")

world.create_world(700, 700)
world.set_back_color(150, 215, 255)
snowlist = []

mode = True


@wrap.always(2000)
def water():
    snowlist.append(drop.Drop(random.randint(20, 680), -5))


@wrap.always(1000)
def snowflake():
    snowlist.append(snowflakeclass.Snowflake(random.randint(20, 680), -5, mode))


@wrap.always(10)
def down():
    for snowflake in snowlist:
        snowflake.movedown()


@wrap.on_key_down(wrap.K_SPACE)
def square():
    global mode
    for snowflake in snowlist:
        if type(snowflake)==drop.Drop:
            snowflake.square(spritetext="Я КАПЛЯ")
        else:
            snowflake.square()
            mode = False


@wrap.on_key_down(wrap.K_ESCAPE)
def normal():
    global mode
    for snowflake in snowlist:
        if hasattr(snowflake, "normal"):
            snowflake.normal()
            mode = True



