import time
import random
import threading
import minecraftstuff as minecraftstuff


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

ARENAX = 10
ARENAZ = 20
ARENAY = 3

def createArena(pos):
    #Создаём игровое поле из травы
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1,
                 2)
    # Создаём стеклянные стенки
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,
                 20)

    mc.setBlocks(pos.x, pos.y + 1, pos.z,
                 pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ,
                 0)

def theWall(arenaPos, wallZPos):
    #Определяем координаты стены относительно арены
    wallPos = arenaPos.clone()
    wallPos.y += 1
    wallPos.z += wallZPos
    #Создаём каркас для стены
    wallShape = minecraftstuff.MinecraftShape(mc, wallPos)
    # Заполняем каркас блоками
    wallShape.setBlocks(0, 1, 0,  # точка начала установки блоков
                        ARENAX, ARENAY - 1, 0,  # точка конца установки блоков
                        45)
    while not gameOver:
        wallShape.moveBy(0, 1, 0)
        time.sleep(1)
        wallShape.moveBy(0, -1, 0)
        time.sleep(1)

def theRiver(arenaPos, riverZPos):
    RIVERWIDTH = 4                  #Ширина рва
    BRIDGEWIDTH = 2                 #Ширина платформы
    # Создаём ров и заполняем его водой
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                arenaPos.x + ARENAX, arenaPos.y,
                arenaPos.z + riverZPos + RIVERWIDTH - 1,
                0)
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y - 2,
                 arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 8)

    # Получаем координаты платформы и перемещаем её
    bridgePos = arenaPos.clone()
    bridgePos.z += riverZPos + 1
    bridgeShape = minecraftstuff.MinecraftShape(mc, bridgePos)
    bridgeShape.setBlocks(0, 0, 0,
                          BRIDGEWIDTH - 1, 0, RIVERWIDTH - 3,
                          5)
    steps = ARENAX - BRIDGEWIDTH + 1
    while not gameOver:
        for left in range(0, steps):
            bridgeShape.moveBy(1, 0, 0)
            time.sleep(1)
        for right in range(0, steps):
            bridgeShape.moveBy(-1, 0, 0)
            time.sleep(1)

def theHoles(arenaPos, holesZPos):     #Функция для создания ям
    HOLES = 15                          #Количество ям
    HOLESWIDTH = 3                      #Глубина ям
    holePos = arenaPos.clone()          #клонируем координаты арены
    while not gameOver:
        holes = []                      #Список с координатами ям
        for count in range(0, HOLES):
            x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
            z = random.randint(arenaPos.z + holesZPos, arenaPos.z + holesZPos + HOLESWIDTH)
            holePos.x = x
            holePos.z = z
            holes.append(holePos.clone())#добавляем координаты новой ямы в список
        for hole in holes:
            mc.setBlock(hole.x, hole.y, hole.z, 35, 15)  #Помечаем чёрной шерстью
        time.sleep(0.25)

        for hole in holes:              #Создаём ямы
            mc.setBlocks(hole.x, hole.y, hole.z, hole.x, hole.y - 2, hole.z, 0)
        time.sleep(2)

        for hole in holes:              #Закапываем ямы
            mc.setBlocks(hole.x, hole.y, hole.z, hole.x, hole.y - 2, hole.z, 2)
        time.sleep(2)

def createDiamonds(arenaPos, number):   #Функция создания алмазов
    for diamond in range(0, number):
        x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
