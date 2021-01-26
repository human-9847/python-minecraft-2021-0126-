from mcpi.minecraft import Minecraft
we =Minecraft.create()
x,y,z = we.player.getTilePos()
we.setSign(x,y,z+1,63,0,"看到的人是笨蛋")