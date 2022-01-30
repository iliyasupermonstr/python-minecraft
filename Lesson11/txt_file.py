# Открываем (или создаём) файл на перезапись (w)
secretFile = open("file.txt", "w", encoding="utf-8")
secretFile.write("Это секретный файл! Тихо. Чур никому не рассказывать. \n")
secretFile.close()

# Открываем тот же файл в режиме добавления (a)
secretFile = open("file.txt", "a", encoding="utf-8")
secretFile.write("О, теперь  я всё исправил!")
secretFile.close()

# Открываем этот файл на чтение (r)
secretFile = open("file.txt", "r", encoding="utf-8")
text = secretFile.read()
print(text)
secretFile.close()

# w - стирает всё содержимое файла и открывает его для записи
# r - просто открывает файл, чтобы его читать (записывать не получится в таком режиме)
# a - работает так, как и w, но не стирает