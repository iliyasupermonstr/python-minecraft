from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
flowWater = 8
standWater = 9
while True:						              #Бесконечный цикл
  pos = mc.player.getTilePos()
  blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)   #Блок под ногами
  if blockBelow != air and blockBelow !=flowWater and blockBelow !=standWater:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)        #Превращаем в золотой