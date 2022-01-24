import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z
# Создаем список 10 блоков "стекло" (идентификатор 20)
blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
barBlock = 22  # Блок лазурита
count = 0
while count <= len(blocks):  # Устанавливаем столбик из 10 блоков по списку
    for i in range(len(blocks)):
        mc.setBlock(x, y + i, z, blocks[i])

    count += 1
    del blocks[-1]
    blocks.insert(0, barBlock)
    time.sleep(1)

for step in range(len(blocks) - 1, -1, -1):
    count += 1
    blocks[step] = 20
    for i in range(len(blocks)):
        mc.setBlock(x, y + i, z, blocks[i])
    time.sleep(1)



