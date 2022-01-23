from mcpi.minecraft import Minecraft

mc = Minecraft.create()


def setPillar(x, y, z, height):
    stairBlock = 156
    block = 155
    # Вершина колонны
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block, 1)
    mc.setBlock(x - 1, y + height - 1, z, stairBlock, 4)
    mc.setBlock(x + 1, y + height - 1, z, stairBlock, 5)
    mc.setBlock(x, y + height - 1, z + 1, stairBlock, 7)
    mc.setBlock(x, y + height - 1, z - 1, stairBlock, 6)
    # Основание колонны
    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
    mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
    mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
    mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
    mc.setBlock(x, y + 1, z - 1, stairBlock, 2)
    # Ствол колонны
    mc.setBlocks(x, y, z, x, y + height, z, block, 2)


pos = mc.player.getTilePos()
x, y, z = pos.x + 2, pos.y, pos.z

for x in range(0, 50, 5):
    setPillar(pos.x + x, pos.y, pos.z, 12)