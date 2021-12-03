from mcpi.minecraft import Minecraft
import time
import random
import mcpi.block as block

mc = Minecraft.create()

mc.player.setPos(random.randrange(0, 1000), random.randrange(80, 180), random.randrange(0, 1000))
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x - 1, y, z - 1, x + 1, y + 1, z + 1, block.GRASS)
mc.setBlocks(x - 1, y + 1, z - 1, x + 1, y + 2, z + 1, block.FLOWER_YELLOW)

mc.setBlock(x, y + 1, z, block.AIR)


mc.player.setPos(x + 2, y + 2, z + 2)

