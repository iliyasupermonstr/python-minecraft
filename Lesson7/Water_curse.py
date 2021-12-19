import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 30
mc.postToChat("НА ТЕБЕ ВОДНОЕ ПРОКЛЯТИЕ на 30 сек")
while count > 0:
    time.sleep(1)
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    count -= 1
mc.postToChat("Конец проклятия")