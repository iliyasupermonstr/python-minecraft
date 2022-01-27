import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(20)
hits = mc.events.pollBlockHits()

for block in hits:
    x = block.pos.x
    y = block.pos.y
    z = block.pos.z
    mc.player.setTilePos(x, y, z)
    time.sleep(0.5)