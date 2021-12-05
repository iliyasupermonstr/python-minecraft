from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()                    #Получаем позицию игрока

x = pos.x                                       #Извлекаем координату х
y = pos.y                                       #Извлекаем координату у
z = pos.z                                       #Извлекаем координату z

mc.setBlock(x,y, z+1,109, 5)