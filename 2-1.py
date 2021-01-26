from mcpi.minecraft import Minecraft
we =Minecraft.create()
x,y,z, = we.player.getTilePos()

import random,time
while True:
    x,y,z, = we.player.getTilePos()
    color =random.randrange(0,16)
    we.setBlocks(x+12,y,z+12,x-12,y,z-12,95,color)