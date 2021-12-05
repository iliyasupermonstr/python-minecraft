# Игрок над уровнем земли
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()                        #Получаем позицию игрока
x = pos.x                                       #Извлекаем координату х
y = pos.y                                       #Извлекаем координату у
z = pos.z                                       #Извлекаем координату z

highest = mc.getHeight(x, z)                    #Самый высокий блок
mc.postToChat("Высочайший блок на ваших координатах: " + str(highest))