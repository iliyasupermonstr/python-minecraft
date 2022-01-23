import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(10)

hits = mc.events.pollBlockHits()
print(hits)