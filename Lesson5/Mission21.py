from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = -28					 #Координата х дома
buildY = 5						 #Координата y дома
buildZ = -13					 #Координата z дома

width = 10
height = 5
length = 6

pos = mc.player.getTilePos()                    #Получаем позицию игрока
x = pos.x                                       #Извлекаем координату х
y = pos.y                                       #Извлекаем координату y
z = pos.z                                       #Извлекаем координату z


insideX = buildX < x < buildX + width  #Находится ли игрок внутри по Х
insideY =buildY < y < buildY + height
insideZ =buildZ < z < buildZ + length

inHouse = insideX and insideY and insideZ
mc.postToChat('Игрок в доме: ' + str(inHouse))