from mcpi.minecraft import Minecraft
try:
    x = int(input("x="))
    y = int(input("y="))
    z = int(input("z="))
    mc = Minecraft.create()
    mc.player.setTilePos(x, y, z)
    blockType = int(input("Введите ID блока="))

    mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, blockType)

    mc.setBlocks(x + 1, y + 1, z + 1, x + 9, y + 9, z + 9, blockType)
except:
    print("Ошибка вводите именно числа")
