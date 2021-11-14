import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



# Меняем позицию игрока
mc.player.setTilePos(0, 100, 0)
time.sleep(10)
mc.player.setTilePos(498, 756, 4094)
time.sleep(10)
mc.player.setTilePos(826, 756, 473)
time.sleep(10)
mc.player.setTilePos(56.29, 925, 9320)
time.sleep(10)
mc.player.setTilePos(-56.23, 154, 165)