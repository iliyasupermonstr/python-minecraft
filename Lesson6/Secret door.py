from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 150
y = 64
z = 216

mc.setBlock(x+3,y,z-3, 1)          #Установим пьедестал для подарка
gift = mc.getBlock(x+3, y+1, z-3)  #Проверяем блок на пьедестале
if gift != 0:                      #Если пусто
    if gift == 57:                          #Если алмазный блок
        mc.setBlocks(x+3,y,z,x,y+1,z-3,0)   #Делаем проход в дом
        mc.postToChat('Дверь открыта!')
    else:                                   #Иначе
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x,pos.y-1,pos.z,10) #Лава под игроком
        mc.postToChat('Подарок не принят, гори в аду!')
else:                              #Просим положить подарок
    mc.postToChat("Поставьте подарок на пьедестал.")