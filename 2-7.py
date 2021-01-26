from mcpi.minecraft import Minecraft
we =Minecraft.create()
x,y,z, = we.player.getTilePos()
try:
    answer =int(input("請問陛下要放什麼方塊:"))
    we.setBlock(x+1,y,z,answer)
except:
    print("只能輸入數字!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")