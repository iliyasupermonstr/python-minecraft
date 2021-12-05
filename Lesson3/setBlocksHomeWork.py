from mcpi.minecraft import Minecraft
import time
import random
import mcpi.block as block

mc = Minecraft.create()

mc.player.setPos(random.randrange(0, 100), random.randrange(100, 180), random.randrange(0, 100))

pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

platformY = y - 5

mc.setBlocks(x - 1, platformY, z - 1, x + 1, platformY + 1, z + 1, block.GRASS)
mc.setBlocks(x - 1, platformY + 1, z - 1, x + 1, platformY + 2, z + 1, block.FLOWER_YELLOW)

mc.setBlock(x, platformY + 1, z, block.AIR)


