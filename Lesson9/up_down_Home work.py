import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getTilePos()

heights = [pos.y, pos.y]
count = 0

while count < 60:
    pos = mc.player.getTilePos()
    if pos.y < heights[0]:
        heights[0] = pos.y
    elif pos.y > heights[1]:
        heights[1] = pos.y

    count += 1
    time.sleep(1)

mc.postToChat("Низшая позиция: " + str(heights[0]))  # Получаем меньшую высоту
mc.postToChat("Высшая позиция: " + str(heights[1]))  # Получаем большую высоту