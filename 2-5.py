# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:19:03 2021

@author: user
"""

from mcpi.minecraft import Minecraft
we =Minecraft.create()

while True:
    x,y,z = we.player.getTilePos()
    block1 = we.getBlock(x,y-1,z)
    block2 = we.getBlock(x+1,y-1,z)
    block3 = we.getBlock(x-1,y-1,z)
    block4 = we.getBlock(x,y-1,z+1)
    block5 = we.getBlock(x,y-1,z-1)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9\
    or block3 == 8 or block3 == 9 or block4 == 8 or block4 ==9 or block5 == 8 or block5 == 9:
        we.setBlock(x,y-1,z,79)
        we.setBlock(x+1,y-1,z,79)
        we.setBlock(x-1,y-1,z,79)
        we.setBlock(x,y-1,z+1,79)
        we.setBlock(x,y-1,z-1,79)