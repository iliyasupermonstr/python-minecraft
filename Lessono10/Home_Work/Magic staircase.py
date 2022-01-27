from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

x, y, z = pos.x, pos.y, pos.z
stairs = 53

for step in range(10):
    mc.setBlock(x + step, y + step, z, stairs)
    mc.setBlock(x - step, y + step, z, stairs)
    mc.setBlock(x, y + step, z + step, stairs)
    mc.setBlock(x, y + step, z - step, stairs)
