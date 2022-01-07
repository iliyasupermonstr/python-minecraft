from mcpi.minecraft import Minecraft

mc = Minecraft.create()
def happy_ny(name):
    print("С новым 2022 годом!", name)
    mc.postToChat("С новым 2022 годом!" + name)

happy_ny("Максим")
happy_ny("Илья")
happy_ny("Майнкрафт")
happy_ny("Майкрософт")