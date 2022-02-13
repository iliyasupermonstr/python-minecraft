from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import time

class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

    def build(self):
        mc.setBlocks(self.x, self.y, self.z,
                         self.x + self.width, self.y + self.height,
                         self.z + self.depth, 57)
        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,
                         self.x + self.width - 1, self.y + self.height - 1,
                         self.z + self.depth - 1, 0)


    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,
                 self.x + self.width, self.y + self.height,
                 self.z + self.depth, 0)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostHouse = Building(x, y, z, 10, 6, 8)
ghostHouse.build()

time.sleep(30)

ghostHouse.clear()