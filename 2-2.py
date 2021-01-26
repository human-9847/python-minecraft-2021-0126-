
from mcpi.minecraft import Minecraft
we =Minecraft.create()
x,y,z, = we.player.getTilePos()

we.setBlock(x+1,y,z+1,46)
we.setBlock(x-1,y,z+1,46)
we.setBlock(x+1,y,z-1,46)
we.setBlock(x-1,y,z-1,46)
we.setBlock(x,y,z+2,46)
we.setBlock(x,y,z-2,46)
we.setBlock(x-2,y,z,46)
we.setBlock(x+2,y,z,46)
