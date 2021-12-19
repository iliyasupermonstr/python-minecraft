import time

from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()

count = 10
while count > 0:
    mc.postToChat("брат телепортируемся держииииииииииииииись")

    x = random.randint(-200, 200)
    y = random.randint(65, 200)
    z = random.randint(-300, 300)
    mc.player.setPos(x, y, z)
    time.sleep(2)

    count -= 1
mc.postToChat("Конец тура")