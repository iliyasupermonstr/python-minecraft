toDoFile = open('toDoFile.txt', "w", encoding="utf‑8")
toDoList = ""
toDoItem = input("Введите описание дела: ")

while toDoItem != "выход":
    toDoList = toDoItem + " \n"
    toDoFile.write(toDoList)
    toDoItem = input("Введите описание дела: ")
toDoFile.close()