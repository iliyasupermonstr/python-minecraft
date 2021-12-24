from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block

answer = input("Точно хотите построить дом ? (да/нет): ")

if answer == "да":
    pos = mc.player.getPos()
    blockType = 5
    x = pos.x
    y = pos.y
    z = pos.z

    mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, blockType)
    mc.setBlocks(
        x + 1, y + 1, z,  # координата 1-й точки
        x + 9, y + 9, z + 10,  # координата 2-й точки
        block.AIR
    )
    mc.setBlocks(
        x, y + 1, z + 1,  # координата 1-й точки
           x + 10, y + 9, z + 9,  # координата 2-й точки
        block.AIR )

    mc.postToChat("Ахалай махалай БУМ!")