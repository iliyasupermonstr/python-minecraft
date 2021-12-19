from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()                    #Получаем позицию игрока

x = pos.x                                       #Извлекаем координату х
y = pos.y                                       #Извлекаем координату y
z = pos.z                                       #Извлекаем координату z

block = mc.getBlock(x,y-1,z)               #Блок под игроком
block2 = mc.getBlock(x,y+2,z)               #Блок над игроком

inTunnel = block != 0 and block2 != 0   #логическое И
mc.postToChat('Игрок в тоннеле: ' + str(inTunnel))