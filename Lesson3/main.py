from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 0
y = 80
z = 0
block=19
mc.setBlock(x, y, z, block)
mc.setBlock(x, y+1, z, block)
mc.setBlock(x, y+2, z, block)
mc.setBlock(x, y+3, z, block)
