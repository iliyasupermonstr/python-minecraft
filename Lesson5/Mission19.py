# Игрок в воздухе?
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

block = mc.getBlock(x, y-1, z)
mc.postToChat("Игрок находится не в воздухе: " + str(block != 0))