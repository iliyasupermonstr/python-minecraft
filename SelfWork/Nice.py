from mcpi.minecraft import Minecraft
mc = Minecraft.create()
answer = input("Как дела?")
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

if answer == "хорошо":
    mc.setBlocks(x, y , z, x, y+1, z, 10)
    mc.postToChat("ГОРИ В АДУ!!!!!!!")

else:
    mc.setBlocks(x, y , z, x+3, y, z, 57)

    mc.postToChat("На подарок!")
