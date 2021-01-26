from mcpi.minecraft import Minecraft
we =Minecraft.create()

import random
while True:
    x,y,z = we.player.getTilePos()
    color = random.randrange(0,9)
    we.setBlock(x,y,z,18,color)  