from mcpi.minecraft import Minecraft
mc = Minecraft.create()

flowWater = 8
standWater = 9

while True:
  pos = mc.player.getPos()
  block = mc.getBlock(pos.x, pos.y - 1, pos.z)
  if block == flowWater or block == standWater:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 174)