from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

pos = mc.player.getPos()




mc.postToChat("У вас 15 секунд бегите")
time.sleep(15)
mc.postToChat("А вот и не убежал")

mc.player.setPos(pos.x, pos.y, pos.z )