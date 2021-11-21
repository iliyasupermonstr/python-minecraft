from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z
block = 1

mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, 324)

mc.setBlocks(x + 1, y + 1, z + 1, x + 9, y + 9, z + 9, 112)

