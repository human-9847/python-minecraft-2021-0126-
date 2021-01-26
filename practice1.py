from mcpi.minecraft import Minecraft
we =Minecraft.create()

import random
while True:
    x,y,z = we.player.getTilePos()
    block = we.getBlock(x,y-1,z)
    we.setBlock(x,y,z,38,color)  