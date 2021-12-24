from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 172
y = 67
z = 302


# Узнаём id блока в отсеке для подарков
block = mc.getBlock(x, y, z)

if block == 57:
    mc.postToChat("Алмазыыы! БОГИ МАЙНА ДОВОЛЬНЫ")
    mc.setBlock(x, y, z, 0)
elif block == 0:
    mc.postToChat("ГДЕ ПОДАРОК! БОГИ МАЙНКРАФТА РАЗГНЕВАНЫ")
elif block == 3:
    mc.postToChat("ДА КАК ТЫ СМЕЕШЬ? ЗЕМЛЯ? ТЫ БУДЕШЬ НАКАЗАН!")
    mc.player.setPos(0, 0, 0)
    mc.setBlock(x, y, z, 0)
else:
    mc.postToChat("Спасибо за подарок, смертный!")
    mc.setBlock(x, y, z, 0)