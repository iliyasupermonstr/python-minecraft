import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



# Меняем позицию игрока
mc.player.setTilePos(0, 80, 0)
time.sleep(10)
mc.player.setTilePos(498, 80, 4094)
time.sleep(10)
mc.player.setTilePos(826, 70, 473)
time.sleep(10)
mc.player.setTilePos(56.29, 80, 9320)
time.sleep(10)
mc.player.setTilePos(-56.23, 70, 165)
