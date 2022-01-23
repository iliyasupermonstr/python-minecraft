from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()



stairs = 53

count = 0
while count < 10:
    mc.setBlocks(x + count, y + count, z, stairs)
    count += 1