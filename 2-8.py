from mcpi.minecraft import Minecraft
we =Minecraft.create()
userName = ("請輸入姓名:")
message = ("請輸入發言:")
we.postToChat("<"+userName+">"+message)