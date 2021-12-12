from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Точно бахнуть хотите? (да/нет): ")

if answer == "да":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x-1, pos.y-1, pos.z-1,
                 pos.x+1, pos.y+1, pos.z+1,
                 0)
    mc.postToChat("БАБАХ")