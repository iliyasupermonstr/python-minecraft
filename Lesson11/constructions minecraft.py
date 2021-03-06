import pickle
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def sortPair(val1, val2):
   if val1 > val2:
       return val2, val1
   else:
       return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
   # Получаем максимальные и минимальные значения x, y и z
   x1, x2 = sortPair(x1, x2)
   y1, y2 = sortPair(y1, y2)
   z1, z2 = sortPair(z1, z2)
   width = x2 - x1
   height = y2 - y1
   length = z2 - z1
   structure = []
   print("Пожалуйста, подождите…")
   # Копируем конструкцию
   for row in range(height):
       structure.append([])
       for column in range(width):
           structure[row].append([])
           for depth in range(length):
               block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
               structure[row][column].append(block)
   return structure

# Получаем координаты первого угла
input("Пройдите к первому углу и нажмите Enter в этом окне")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

# Получаем координаты второго (противоположного) угла
input("Пройдите к противоположному углу и нажмите Enter в этом окне")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

print("Копируем в файл")
structure = copyStructure(x1, y1, z1, x2, y2, z2)

# Сохраняем конструкцию в файл
pickleFile = open("pickleFile", "wb")
pickle.dump(structure, pickleFile