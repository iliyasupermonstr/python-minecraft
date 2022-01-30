from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open('toDoFile.txt', "r", encoding="utf‑8")

for line in toDoList:
    mc.postToChat(line)