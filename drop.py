import wrap,random
from wrap import sprite,sprite_text

class Drop():
    def __init__(self, x, y):
        self.id = sprite.add("drop", x, y, "WATER")
        self.text = sprite.add_text("2", x, y, back_color=[254, 75, 255],visible=False)

    def movedown(self):
        sprite.move(self.id, 0, 2)
        sprite.move(self.text, 0, 2)

    def square(self,spritetext="empty"):

        sprite_text.set_text(self.text,spritetext)
        sprite.hide(self.id)
        sprite.show(self.text)

