

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z


answer = input("Вы хотите повернуть блок? д/н :")
blockType = int(input("Введите айди блока"))

if answer == "д":
    mc.setBlock(x, y, z + 1, blockType, True)
    print("Блок установлен и повёрнут")
else:
    mc.setBlock(x, y, z + 1, blockType, False)
    print("Блок установлен без поворота")
