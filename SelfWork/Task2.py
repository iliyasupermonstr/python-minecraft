from mcpi.minecraft import Minecraft
import random
import mcpi.block as block

mc = Minecraft.create()
mc.player.setTilePos(random.randrange(0, 100), random.randrange(100, 180), random.randrange(0, 100))

pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z
blockType = block.BRICK_BLOCK

mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, blockType)
mc.setBlocks(
    x+1, y+1, z,  # координата 1-й точки
    x + 9, y + 9, z + 10,  # координата 2-й точки
    block.AIR
)
mc.setBlocks(
    x, y+1, z+1,  # координата 1-й точки
    x + 10, y + 9, z + 9,  # координата 2-й точки
    block.AIR
)