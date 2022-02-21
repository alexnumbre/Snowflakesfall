import wrap,random
from wrap import sprite

def createsnowflake():
    x = random.randint(20, 680)
    y = -5
    snowflake = sprite.add("snow", x, y, "snow")
    snowflakeA = {"id": snowflake, "speed": random.randint(1, 10)}
    return snowflakeA