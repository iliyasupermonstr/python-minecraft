from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 172
y = 67
z = 302


# Узнаём id блока в отсеке для подарков
block = mc.getBlock(x, y, z)

if block == 41:
    mc.postToChat("Ураааааа! Я БОГАЧ")
    mc.setBlock(x, y, z, 0)



elif block == 103 :
    mc.postToChat("Вкусный арбуз спасибо за еду!")
mc.setBlock(x, y, z, 0)