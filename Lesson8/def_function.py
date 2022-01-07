from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def lol():
    print("Привет")
    print("Приятно познакомится")
    mc.postToChat("Привет!")
    mc.postToChat("Приятно познакомиться!")

lol()

