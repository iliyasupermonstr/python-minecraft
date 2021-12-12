zombie = int(input("Сколько ты видишь зомби :"))
if zombie > 20:
    print("Ого! Осторожно не умри!")
elif zombie == 0:
    print("Э! А где все то?")
elif zombie < 0:
    print ("А такое вообще бывает ?")
else:
    print("Зобми вам конец!")