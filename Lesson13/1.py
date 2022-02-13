from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Location(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

river = Location(100, 70, -100)

mc.player.setTilePos(river.x, river.y, river.z)