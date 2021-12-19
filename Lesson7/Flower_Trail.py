from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y-1, pos.z, random.randint(1 , 70))