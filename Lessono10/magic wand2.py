import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(60)
hits = mc.events.pollBlockHits()

for block in hits:
    x = block.pos.x
    y = block.pos.y
    z = block.pos.z
    mc.setBlock(x, y, z, 103)