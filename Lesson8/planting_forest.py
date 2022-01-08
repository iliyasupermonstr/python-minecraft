from mcpi.minecraft import Minecraft

mc = Minecraft.create()


def growTree(x, y, z):
    mc.setBlocks(x, y, z, x + 1, y + 1, z + 1, 2)
    mc.setBlocks(x, y, z, x, y + 7, z, 17)
    mc.setBlocks(x - 3, y + 8, z - 3, x + 3, y + 8, z + 3, 161.1 )
    mc.setBlocks(x - 2, y + 9, z - 2, x + 2, y + 9, z + 2, 161.1)


pos = mc.player.getTilePos()

growTree(pos.x + 2, pos.y, pos.z)
