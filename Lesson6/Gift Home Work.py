from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time



x = 172
y = 67
z = 302


mc.postToChat("Поставьте блок на королевский пьедистал!(У тебе есть пять секунд время пошло!)")

mc.postToChat("5")
time.sleep(1)
mc.postToChat("4")
time.sleep(1)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1 Началось Надеюсь положил подарок иначе зарежу!")
time.sleep(1)

# Узнаём id блока в отсеке для подарков
block = mc.getBlock(x, y, z)

if block == 41:
    mc.postToChat("Ураааааа! Я БОГАЧ")
    mc.setBlock(x, y, z, 0)



elif block == 103 :
    mc.postToChat("Вкусный арбуз спасибо за еду!")
mc.setBlock(x, y, z, 0)