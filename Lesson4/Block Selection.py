from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = input("Введите ID блока")
blockType = int(blockType)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)