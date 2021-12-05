# Игрок в воде?
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

block = mc.getBlock(x, y, z)
mc.postToChat("Игрок в воде: " + str(block == 8))