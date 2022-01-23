from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

B =(35, 15)
W = 25
R = (35, 14)

list = [[W, W, W, W],
        [B, W, W, B],
        [W, B, B,W],
        [B, B, B, B]]

for block_y in range(4):
    for block_x in range(4):
        mc.setBlock(x+block_x, y-block_y+4, z,list[block_y][block_x])


